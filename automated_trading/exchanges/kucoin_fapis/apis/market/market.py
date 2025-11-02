from automated_trading.exchanges.kucoin_fapis.apis.base_api import BaseFutureApi
from aiohttp import ClientSession
from . import _model


class MarketApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    async def aget_symbol_info(self, session: ClientSession, symbol: str):
        model = _model.GetSymbol()

        payload = self.prepare_get_payload(
            endpoint=model.endpoint.format(symbol=symbol),
            query_params=b"",
        )
        response = await session.request(**payload)
        return response
