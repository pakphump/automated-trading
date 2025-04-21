from automated_trading import AutomatedTrading
from automated_trading.binance_apis import *
import functions_framework
from flask import Request
import time

automated_trading = AutomatedTrading()


@functions_framework.http
def cdc_strategy_handler(request: Request):

    request_json = request.get_json()
    print(request_json)

    # Experiment
    order_params = {
        "symbol": request_json["symbol"],
        "quantity": request_json["quantity"],
        "api_key": request_json["api_key"],
        "secret_key": request_json["secret_key"],
    }

    # Open Long orders
    open_long_order(**order_params)
    time.sleep(1)
    open_short_order(**order_params)
    time.sleep(1)
    close_long_order(**order_params)
    time.sleep(1)
    close_short_order(**order_params)

    return order_params
