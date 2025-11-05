import aiohttp
from automated_trading.exchanges import KucoinFutureApiManager
from automated_trading.strategies import apply_cdc_strategy
from automated_trading.constants import PositionAction, CDC_STRATEGY_RESULT
from typing import Literal
from automated_trading import utils


class AutomatedTrading:
    async def run_cdc_strategy(
        self,
        session: aiohttp.ClientSession,
        api_config: dict,
        exchange: Literal["kucoin"],
        symbol: str,
        timeframe: int,
        qty: str,
        **kw,
    ):
        if exchange != "kucoin":
            raise ValueError(f"CDC Strategy Not support {exchange} exchange")

        client_id = f"cdc_strategy_{symbol}"
        leverage = kw.get("leverage", 125)
        kucoin_manager = KucoinFutureApiManager(**api_config)

        # Get Kline
        kline_df = await kucoin_manager.aget_klines(
            session,
            symbol=symbol,
            timeframe=timeframe,
            n_records=510,
            end=utils.get_current_utc_timestamp_ms(),
        )

        cdc_action = apply_cdc_strategy(kline_df)

        # If Hold Action
        if cdc_action in [
            PositionAction.HOLD_LONG.value,
            PositionAction.HOLD_SHORT.value,
        ]:
            return CDC_STRATEGY_RESULT.format(symbol=symbol, action=cdc_action)

        # Get Current Position
        position_list = await kucoin_manager.aget_position_lists(session=session)
        if position_list:
            # Close Current Position
            closed_position = await kucoin_manager.apost_close_order(
                session=session, client_id=client_id, symbol=symbol
            )
            print("closed position", closed_position)

        if cdc_action == PositionAction.OPEN_LONG.value:
            opened_position = await kucoin_manager.aplace_order(
                session=session,
                client_id=client_id,
                side="buy",
                type="market",
                qty=qty,
                leverage=leverage,
            )

        elif cdc_action == PositionAction.OPEN_SHORT.value:
            opened_position = await kucoin_manager.aplace_order(
                session=session,
                client_id=client_id,
                side="sell",
                type="market",
                qty=qty,
                leverage=leverage,
            )
        else:
            raise ValueError(f"Error Not Support {cdc_action} action")

        print("opened position", opened_position)

        return CDC_STRATEGY_RESULT.format(symbol=symbol, action=cdc_action)
