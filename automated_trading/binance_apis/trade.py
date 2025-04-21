from automated_trading.binance_apis.market_data import get_server_time
from automated_trading.models import *
from automated_trading.utils import add_signature_in_payload
import requests


def post_change_position_mode(api_key: str, secret_key: str, dual_side_position: bool):

    server_time = get_server_time()

    url_n_method = PostChangePositionMode().model_dump(by_alias=True)
    payload = PostChangePositionModeRequest(
        dual_side_position=dual_side_position, timestamp=server_time
    )

    # Add signature
    payload = add_signature_in_payload(secret_key, payload)
    headers = {"X-MBX-APIKEY": api_key}

    response = requests.request(**url_n_method, params=payload, headers=headers)

    return response.status_code


def open_long_position():
    pass


def close_long_position():
    pass


def open_short_position():
    pass


def close_short_position():
    pass
