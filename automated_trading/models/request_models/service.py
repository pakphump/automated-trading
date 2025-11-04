from typing import List, Literal, Union
from pydantic import BaseModel, Field


class ApiConfig(BaseModel):
    api_key: str
    api_secret: str
    api_passphrase: str | None = None


class CdcBotParams(BaseModel):
    bot_type: Literal["cdc_strategy"]
    exchange: Literal["kucoin"]
    symbol: str
    timeframe: int
    qty: str
    leverage: int


class TurtleBotParams(BaseModel):
    bot_type: Literal["turtle_strategy"]


class Bot(BaseModel):
    api_config: ApiConfig
    bot_params: Union[CdcBotParams, TurtleBotParams] = Field(discriminator="type")


class AutomatedTradingRequest(BaseModel):
    bots: List[Bot]
