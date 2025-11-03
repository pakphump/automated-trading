import aiohttp
from automated_trading.exchanges import KucoinFutureApiManager
from automated_trading.strategies import apply_cdc_strategy
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

        kucoin_manager = KucoinFutureApiManager(**api_config)

        # Get Kline
        kline_df = await kucoin_manager.aget_klines(
            session,
            symbol=symbol,
            timeframe=timeframe,
            n_records=510,
            end=utils.get_current_utc_timestamp_ms(),
        )

        action = apply_cdc_strategy(kline_df)
        return action


# class AutomatedTrading:
#     def __init__(self):
#         pass

#     def run_cdc_strategy(
#         self, symbol: str, interval: str, quantity: float, api_key: str, secret_key: str
#     ):

#         # # Check position mode
#         # current_position_model = get_current_position_mode(api_key, secret_key)
#         # if current_position_model is False:
#         #     post_change_position_mode(api_key, secret_key, dual_side_position=True)

#         # Get Kline data
#         kline_list = get_continuous_klines(symbol=symbol, interval=interval)
#         kline_df = preprocess_klines_data(kline_list)

#         cdc_action = process_cdc_strategy(kline_df)

#         print("Current Datetime", datetime.now())
#         print("CDC Action", cdc_action)

#         # If cdc action in ["hold_long", "hold_short"]
#         if cdc_action in ["hold_long", "hold_short"]:

#             response = CdcStrategyHandlerResponse(
#                 datetime=datetime.now(), action=cdc_action
#             )

#             return response.model_dump()

#         # Get current position
#         current_position = get_current_position_order_by_symbol(
#             symbol=symbol, api_key=api_key, secret_key=secret_key
#         )

#         order_params = {
#             "symbol": symbol,
#             "quantity": quantity,
#             "api_key": api_key,
#             "secret_key": secret_key,
#         }

#         if cdc_action == "open_long":

#             if current_position is not None:
#                 close_short_order(**order_params)
#                 print(" - Close Short Order")

#             open_long_order(**order_params)
#             print(" - Open Long Order")

#         elif cdc_action == "open_short":

#             if current_position is not None:
#                 close_long_order(**order_params)
#                 print(" - Close Long Order")

#             open_short_order(**order_params)
#             print(" - Open Short Order")

#         return CdcStrategyHandlerResponse(
#             datetime=datetime.now(), action=cdc_action
#         ).model_dump()
