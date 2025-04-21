from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import List


class GetServerTimeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    server_time: int


class GetCurrentPositionModeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    dual_side_position: bool


class _positions(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    symbol: str
    position_side: str


class GetCurrentPositionOrderResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    positions: List[_positions]
