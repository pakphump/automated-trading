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
        atr_multiplier: float,
        risk_pct: float,
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

        cdc_action, current_price, stoploss_price = apply_cdc_strategy(
            kline_df,
            atr_multiplier,
        )

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

        # Get current capital
        capital = await kucoin_manager.aget_account_funding(session, "USDT")
        capital = capital["accountEquity"]

        # Get coin_detail
        coin_detail = await kucoin_manager.aget_symbol_info(session, symbol)
        coin_multiplier = coin_detail["multiplier"]

        if cdc_action == PositionAction.OPEN_LONG.value:

            qty_size = utils.calculate_qty_size(
                capital, risk_pct, current_price, stoploss_price, coin_multiplier
            )

            print("qty_size", qty_size)
            print("SL price", stoploss_price)

            opened_position = await kucoin_manager.aplace_st_order(
                session=session,
                client_id=client_id,
                symbol=symbol,
                side="buy",
                type="market",
                qty=qty_size,
                leverage=leverage,
                trigger_stop_down_price=str(stoploss_price),
            )

        elif cdc_action == PositionAction.OPEN_SHORT.value:

            qty_size = utils.calculate_qty_size(
                capital, risk_pct, current_price, stoploss_price, coin_multiplier
            )

            print("qty_size", qty_size)
            print("SL price", stoploss_price)

            opened_position = await kucoin_manager.aplace_st_order(
                session=session,
                client_id=client_id,
                symbol=symbol,
                side="sell",
                type="market",
                qty=qty_size,
                leverage=leverage,
                trigger_stop_up_price=str(stoploss_price),
            )
        else:
            raise ValueError(f"Error Not Support {cdc_action} action")

        print("opened position", opened_position)

        return CDC_STRATEGY_RESULT.format(symbol=symbol, action=cdc_action)
