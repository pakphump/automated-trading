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
    response = open_long_order(**order_params)
    print("--- Open Long---")
    print(response.json())
    print("----------------\n")
    time.sleep(1)

    response = open_short_order(**order_params)
    print("--- Open Short---")
    print(response.json())
    print("----------------\n")
    time.sleep(1)

    response = close_long_order(**order_params)
    print("--- Close Long---")
    print(response.json())
    print("----------------\n")
    time.sleep(1)

    response = close_short_order(**order_params)
    print("--- Close Short---")
    print(response.json())
    print("----------------\n")

    return order_params
