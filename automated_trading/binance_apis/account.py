import requests
from automated_trading.utils import create_signature
from automated_trading.binance_apis.market_data import get_server_time
from automated_trading.models import *


def get_current_position_mode(api_key: str, secret_ket: str):

    server_time = get_server_time()

    url_n_method = GetCurrentPositionMode().model_dump(by_alias=True)
    payload = GetCurrentPositionModeRequest(timestamp=server_time).model_dump(
        by_alias=True
    )

    # Add signature
    signature = create_signature(secret_ket, payload)
    payload["signature"] = signature

    headers = {"X-MBX-APIKEY": api_key}

    response = requests.request(**url_n_method, params=payload, headers=headers)

    return response.json()
