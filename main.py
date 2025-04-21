from automated_trading import AutomatedTrading
from automated_trading.binance_apis import *
import functions_framework
from flask import Request

automated_trading = AutomatedTrading()


@functions_framework.http
def cdc_strategy_handler(request: Request):

    request_json = request.get_json()

    response = automated_trading.run_cdc_strategy(
        symbol=request_json["symbol"],
        interval=request_json["interval"],
        quantity=request_json["quantity"],
        api_key=request_json["api_key"],
        secret_key=request_json["secret_key"],
    )

    return response
