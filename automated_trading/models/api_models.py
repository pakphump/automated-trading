from pydantic import BaseModel, Field, ConfigDict
from automated_trading.constants import BINANCE_FUTURE_BASE_URL


class BinanceHeader(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    x_mbx_apikey: str = Field(alias="X-MBX-APIKEY")


class GetServerTime(BaseModel):
    method: str = "GET"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/time"


class GetContinuousKlines(BaseModel):
    method: str = "GET"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/continuousKlines"


class GetCurrentPositionMode(BaseModel):
    method: str = "GET"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/positionSide/dual"


class GetCurrentPositionOrder(BaseModel):
    method: str = "GET"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v3/account"


class PostChangePositionMode(BaseModel):
    method: str = "POST"
    utl: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/positionSide/dual"


class PostOrder(BaseModel):
    method: str = "POST"
    url: str = f"{BINANCE_FUTURE_BASE_URL}/fapi/v1/order"
