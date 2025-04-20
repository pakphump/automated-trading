from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class GetServerTimeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    server_time: int
