class AccountEndpoint:
    GET_ACCOUNT_FUNDING = "/api/v1/account-overview"


class MarketEndpoint:
    GET_SYMBOL = "/api/v1/contracts/{symbol}"
    GET_ALL_SYMBOL_ACTIVE = "/api/v1/contracts/active"
    GET_KLINES = "/api/v1/kline/query"


class OrderEndpoint:
    POST_CREATE_ORDER = "/api/v1/orders"
    POST_CREATE_ORDER_TEST = "/api/v1/orders/test"
    POST_CREATE_ST_ORDER = "/api/v1/st-orders"
    GET_ORDER_LIST = "/api/v1/orders"


class PositionEndpoint:
    GET_POSITION_LIST = "/api/v1/positions"
