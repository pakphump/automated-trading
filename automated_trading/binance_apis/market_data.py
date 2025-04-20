import requests
from automated_trading.models import *


def get_server_time() -> float:

    url_n_method = GetServerTime().model_dump(by_alias=True)

    response = requests.request(**url_n_method)
    response.raise_for_status()

    response_model = GetServerTimeResponse(**response.json())
    return response_model.server_time


def get_continuous_klines(
    symbol: str, interval: str, limit: Optional[int] = None
) -> list:

    url_n_method = GetContinuousKlines().model_dump(by_alias=True)

    payload = GetContinuousKlinesRequest(
        pair=symbol, interval=interval, limit=limit
    ).model_dump(by_alias=True)

    response = requests.request(**url_n_method, params=payload)
    response.raise_for_status()

    return response.json()
