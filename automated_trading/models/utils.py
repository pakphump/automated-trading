from pydantic import BaseModel, ConfigDict
from automated_trading.constants import ApiMethod


class GetMethodBaseModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    method: ApiMethod = ApiMethod.GET


class PostMethodBaseModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    method: ApiMethod = ApiMethod.POST
