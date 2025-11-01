from automated_trading.models import GetMethodBaseModel


class GetAccountFunding(GetMethodBaseModel):
    endpoint: str = "/api/v1/account-overview"
