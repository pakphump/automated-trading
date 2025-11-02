from .apis import AccountApi, MarketApi


class KucoinFutureApiManager(AccountApi, MarketApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)
