from automated_trading.models import PostMethodBaseModel


class PostCreateOrder(PostMethodBaseModel):
    endpoint: str = "/api/v1/orders"


class PostCreateOrderTest(PostMethodBaseModel):
    endpoint: str = "/api/v1/orders/test"
