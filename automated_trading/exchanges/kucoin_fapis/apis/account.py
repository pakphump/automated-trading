from ._base_api import BaseFutureApi
from ._endpoints import AccountEndpoint
from aiohttp import ClientSession


class AccountApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    async def aget_account_funding(self, session: ClientSession, currency: str):

        payload = self.prepare_get_payload(
            endpoint=AccountEndpoint.GET_ACCOUNT_FUNDING,
            query_params={"currency": currency},
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result["data"]
