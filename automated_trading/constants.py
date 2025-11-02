from enum import StrEnum


class ApiMethod(StrEnum):
    GET = "GET"
    POST = "POST"


BINANCE_FUTURE_BASE_URL = "https://fapi.binance.com"
KUCOIN_FUTURE_BASE_URI = "https://api-futures.kucoin.com"
KUCOIN_KLINE_COLUMNS = ["time", "open", "high", "low", "close", "lots", "volume"]
KLINE_FLOAT_COLUMNS = ["open", "high", "low", "close", "volume"]
KLINE_COLUMNS = [
    "time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_asset_vol",
    "no_trade",
    "taker_buy_base",
    "taker_buy_quote",
    "ignore",
]
