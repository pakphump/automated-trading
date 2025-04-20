from automated_trading import AutomatedTrading
from automated_trading.binance_apis.account import get_current_position_mode
from automated_trading.models import CdcStrategyHandlerRequest
from datetime import datetime
import functions_framework
from flask import Request

automated_trading = AutomatedTrading()


@functions_framework.http
def cdc_strategy_handler(request: Request):

    request_json = request.get_json()
    print(request_json)

    # request_model = CdcStrategyHandlerRequest(**request_json)

    # result = automated_trading.run_cdc_strategy(
    #     symbol=request_model.symbol, interval=request_model.interval
    # )

    response = get_current_position_mode(
        request_json["api_key"], request_json["secret_ket"]
    )

    return response
