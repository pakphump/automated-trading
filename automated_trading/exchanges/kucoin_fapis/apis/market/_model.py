from automated_trading.models import GetMethodBaseModel


class GetSymbol(GetMethodBaseModel):
    endpoint: str = "/api/v1/contracts/{symbol}"


class GetAllSymbolActive(GetMethodBaseModel):
    endpoint: str = "/api/v1/contracts/active"


class GetKlines(GetMethodBaseModel):
    endpoint: str = "/api/v1/kline/query"
