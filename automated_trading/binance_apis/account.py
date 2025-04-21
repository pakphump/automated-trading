import requests
from automated_trading.utils import add_signature_in_payload
from automated_trading.binance_apis.market_data import get_server_time
from automated_trading.models import *


def get_current_position_mode(api_key: str, secret_key: str) -> bool:

    server_time = get_server_time()

    url_n_method = GetCurrentPositionMode().model_dump(by_alias=True)
    payload = GetCurrentPositionModeRequest(timestamp=server_time).model_dump(
        by_alias=True
    )

    # Add signature
    payload = add_signature_in_payload(secret_key, payload)
    headers = {"X-MBX-APIKEY": api_key}

    response = requests.request(**url_n_method, params=payload, headers=headers)
    response.raise_for_status()

    response_model = GetCurrentPositionModeResponse(**response.json())

    return response_model.dual_side_position
