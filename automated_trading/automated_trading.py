from automated_trading.binance_apis import *
from automated_trading.models import *
from automated_trading.preprocessor import preprocess_klines_data
from automated_trading.strategies import process_cdc_strategy
from datetime import datetime


class AutomatedTrading:
    def __init__(self):
        pass

    def run_cdc_strategy(
        self, symbol: str, interval: str, quantity: float, api_key: str, secret_key: str
    ):

        # Check position mode
        current_position_model = get_current_position_mode(api_key, secret_key)
        if current_position_model is False:
            post_change_position_mode(api_key, secret_key, dual_side_position=True)

        # Get Kline data
        kline_list = get_continuous_klines(symbol=symbol, interval=interval)
        kline_df = preprocess_klines_data(kline_list)

        cdc_action = process_cdc_strategy(kline_df)

        # If cdc action in ["hold_long", "hold_short"]
        if cdc_action in ["hold_long", "hold_short"]:

            response = CdcStrategyHandlerResponse(
                datetime=datetime.now(), action=cdc_action
            )

            return response.model_dump()

        # Get current position
        current_position = get_current_position_order_by_symbol(
            symbol=symbol, api_key=api_key, secret_key=secret_key
        )

        order_params = {
            "symbol": symbol,
            "quantity": quantity,
            "api_key": api_key,
            "secret_key": secret_key,
        }

        if cdc_action == "open_long":

            if current_position is not None:
                close_short_order(**order_params)

            open_long_order(**order_params)

        elif cdc_action == "open_short":

            if current_position is not None:
                close_long_order(**order_params)

            open_short_order(**order_params)

        return CdcStrategyHandlerResponse(
            datetime=datetime.now(), action=cdc_action
        ).model_dump()
