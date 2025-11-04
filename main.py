import functions_framework.aio
import aiohttp
import asyncio
from automated_trading import AutomatedTrading
from automated_trading.models import AutomatedTradingRequest

automated_trading = AutomatedTrading()


@functions_framework.aio.http
async def automated_trading_handler(request):
    request_obj = await request.json()
    request_model = AutomatedTradingRequest(**request_obj)

    tasks = []
    async with aiohttp.ClientSession() as session:
        for bot_obj in request_model.bots:

            if bot_obj.bot_params.bot_type == "cdc_strategy":

                tasks.append(
                    automated_trading.run_cdc_strategy(
                        session=session,
                        api_config=bot_obj.api_config.model_dump(),
                        **bot_obj.bot_params.model_dump()
                    )
                )

        result = await asyncio.gather(*tasks)
        print("####")
        print(result)
        print("####")
    return {"success": 200}
