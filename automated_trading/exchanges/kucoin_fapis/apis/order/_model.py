from automated_trading.models import PostMethodBaseModel, GetMethodBaseModel


class PostCreateOrder(PostMethodBaseModel):
    endpoint: str = "/api/v1/orders"


class PostCreateOrderTest(PostMethodBaseModel):
    endpoint: str = "/api/v1/orders/test"


class PostCreateStOrder(PostMethodBaseModel):
    endpoint: str = "/api/v1/st-orders"


class GetOrderList(GetMethodBaseModel):
    endpoint: str = "/api/v1/orders"
