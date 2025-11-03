# from automated_trading import AutomatedTrading
# from automated_trading.exchanges.binance_apis import *
import functions_framework
from flask import Request
import aiohttp
from automated_trading.exchanges.kucoin_fapis import KucoinFutureApiManager

# automated_trading = AutomatedTrading()


# @functions_framework.http
# def cdc_strategy_handler(request: Request):

#     request_json = request.get_json()

#     response = automated_trading.run_cdc_strategy(
#         symbol=request_json["symbol"],
#         interval=request_json["interval"],
#         quantity=request_json["quantity"],
#         api_key=request_json["api_key"],
#         secret_key=request_json["secret_key"],
#     )

# return response


@functions_framework.http
async def automated_trading_handler(request: Request):
    async with aiohttp.ClientSession() as session:

        for bot_obj in request["bot_list"]:

            kucoin_api_manager = KucoinFutureApiManager(
                api_key=bot_obj["api_key"],
                api_secret=bot_obj["api_secret"],
                api_passphrase=bot_obj["api_passphrase"],
            )

            account = await kucoin_api_manager.aget_account_funding(session, "USDT")

    print(account)
    return {"account": account}
