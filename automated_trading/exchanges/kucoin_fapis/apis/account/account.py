from automated_trading.exchanges.kucoin_fapis.apis.base_api import BaseFutureApi
from . import _model


class AccountApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    async def get_account_funding(self, session, currency: str):
        model = _model.GetAccountFunding()

        payload = self.prepare_get_payload(
            endpoint=model.endpoint,
            query_params={"currency": currency},
        )
        response = await session.request(**payload)
        return response
