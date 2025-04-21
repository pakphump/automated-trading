from automated_trading.binance_apis.market_data import get_server_time
from automated_trading.models import *
from automated_trading.utils import add_signature_in_payload
from typing import Literal
import requests


def post_change_position_mode(api_key: str, secret_key: str, dual_side_position: bool):

    server_time = get_server_time()

    url_n_method = PostChangePositionMode().model_dump(by_alias=True)
    payload = PostChangePositionModeRequest(
        dual_side_position=dual_side_position, timestamp=server_time
    ).model_dump(by_alias=True)

    # Add signature
    payload = add_signature_in_payload(secret_key, payload)
    headers = {"X-MBX-APIKEY": api_key}

    response = requests.request(**url_n_method, params=payload, headers=headers)

    return response.status_code


def post_order(
    symbol: str,
    side: Literal["BUY", "SELL"],
    position_side: Literal["LONG", "SHORT"],
    type: str,
    quantity: float,
    api_key: str,
    secret_key: str,
):

    server_time = get_server_time()
    url_n_method = PostOrder().model_dump(by_alias=True)

    payload = PostOrderRequest(
        symbol=symbol,
        side=side,
        position_side=position_side,
        type=type,
        quantity=quantity,
        timestamp=server_time,
    ).model_dump(by_alias=True)

    # Add signature
    payload = add_signature_in_payload(secret_key, payload)
    headers = {"X-MBX-APIKEY": api_key}

    response = requests.request(**url_n_method, params=payload, headers=headers)

    return response


def open_long_order(symbol: str, quantity: float, api_key: str, secret_key: str):
    response = post_order(
        symbol=symbol,
        side="BUY",
        position_side="LONG",
        type="MARKET",
        quantity=quantity,
        api_key=api_key,
        secret_key=secret_key,
    )

    return response


def close_long_order(symbol: str, quantity: float, api_key: str, secret_key: str):
    response = post_order(
        symbol=symbol,
        side="SELL",
        position_side="LONG",
        type="MARKET",
        quantity=quantity,
        api_key=api_key,
        secret_key=secret_key,
    )

    return response


def open_short_order(symbol: str, quantity: float, api_key: str, secret_key: str):
    response = post_order(
        symbol=symbol,
        side="BUY",
        position_side="SHORT",
        type="MARKET",
        quantity=quantity,
        api_key=api_key,
        secret_key=secret_key,
    )

    return response


def close_short_order(symbol: str, quantity: float, api_key: str, secret_key: str):
    response = post_order(
        symbol=symbol,
        side="SELL",
        position_side="SHORT",
        type="MARKET",
        quantity=quantity,
        api_key=api_key,
        secret_key=secret_key,
    )

    return response
