from automated_trading import AutomatedTrading
from automated_trading.models import CdcStrategyHandlerRequest
from datetime import datetime

automated_trading = AutomatedTrading()


def cdc_strategy_handler(request):
    request_model = CdcStrategyHandlerRequest(**request.json())

    result = automated_trading.run_cdc_strategy(
        symbol=request_model.symbol, interval=request_model.interval
    )

    return {"datetime": datetime.now(), "action": result}
