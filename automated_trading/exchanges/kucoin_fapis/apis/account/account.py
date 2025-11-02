from automated_trading.exchanges.kucoin_fapis.apis.base_api import BaseFutureApi
from aiohttp import ClientSession
from . import _model


class AccountApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    async def aget_account_funding(self, session: ClientSession, currency: str):
        model = _model.GetAccountFunding()

        payload = self.prepare_get_payload(
            endpoint=model.endpoint,
            query_params={"currency": currency},
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result["data"]
