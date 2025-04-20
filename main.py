from automated_trading import AutomatedTrading
from automated_trading.models import CdcStrategyHandlerRequest
from datetime import datetime
import functions_framework
from flask import Request

automated_trading = AutomatedTrading()


@functions_framework.http
def cdc_strategy_handler(request: Request):

    request_json = request.get_json()
    print(request_json)

    request_model = CdcStrategyHandlerRequest(**request_json)

    result = automated_trading.run_cdc_strategy(
        symbol=request_model.symbol, interval=request_model.interval
    )

    return {"datetime": datetime.now(), "action": result}
