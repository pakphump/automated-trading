from automated_trading.exchanges.kucoin_fapis.apis.base_api import BaseFutureApi
from aiohttp import ClientSession
from . import _model


class OrderApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)
