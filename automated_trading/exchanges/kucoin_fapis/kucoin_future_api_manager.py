from .apis import AccountApi, MarketApi, OrderApi, PositionApi


class KucoinFutureApiManager(AccountApi, MarketApi, OrderApi, PositionApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)
