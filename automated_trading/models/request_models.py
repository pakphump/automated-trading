from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import Optional


class GetContinuousKlinesRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    pair: str
    contract_type: str = "PERPETUAL"
    interval: str
    limit: Optional[int] = 500


class PostOrderRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    symbol: str
    side: str
    position_side: str
    type: str
    quantity: float
    recv_window: int = 5000
    timestamp: float
    signature: str


class CdcStrategyHandlerRequest(BaseModel):
    symbol: str
    interval: str
