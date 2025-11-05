from aiohttp import ClientSession
from ._endpoints import PositionEndpoint
from ._base_api import BaseFutureApi
from typing import Literal


class PositionApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    async def aget_position_lists(self, session: ClientSession, currency: str = "USDT"):
        query_params = {"currency": currency}

        payload = self.prepare_get_payload(
            endpoint=PositionEndpoint.GET_POSITION_LIST, query_params=query_params
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result["data"]
