from pydantic import BaseModel
from automated_trading.constants import BINANCE_FUTURE_BASE_URL


class GetServerTime(BaseModel):
    method: str = "GET"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/time"


class GetContinuousKlines(BaseModel):
    method: str = "GET"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/continuousKlines"


class PostOrder(BaseModel):
    method: str = "POST"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/order"
