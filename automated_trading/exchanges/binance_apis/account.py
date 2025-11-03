import requests
from automated_trading.utils import add_signature_in_payload
from automated_trading.exchanges.binance_apis.market_data import get_server_time
from automated_trading.models import *
from automated_trading.preprocessor import extract_current_position_order_by_symbol


def get_current_position_mode(api_key: str, secret_key: str) -> bool:

    server_time = get_server_time()

    url_n_method = GetCurrentPositionMode().model_dump(by_alias=True)
    payload = GetCurrentPositionModeRequest(timestamp=server_time).model_dump(
        by_alias=True
    )

    # Add signature
    payload = add_signature_in_payload(secret_key, payload)
    headers = BinanceHeader(x_mbx_apikey=api_key).model_dump(by_alias=True)

    response = requests.request(**url_n_method, params=payload, headers=headers)
    response.raise_for_status()

    response_model = GetCurrentPositionModeResponse(**response.json())

    return response_model.dual_side_position


def get_current_position_orders(api_key: str, secret_key: str):

    server_time = get_server_time()
    url_n_method = GetCurrentPositionOrder().model_dump(by_alias=True)

    payload = GetCurrentPositionOrderRequest(timestamp=server_time).model_dump(
        by_alias=True
    )

    # Add signature
    payload = add_signature_in_payload(secret_key, payload)
    headers = BinanceHeader(x_mbx_apikey=api_key).model_dump(by_alias=True)

    response = requests.request(**url_n_method, params=payload, headers=headers)
    response.raise_for_status()

    response_json = GetCurrentPositionOrderResponse(**response.json()).model_dump()
    position_orders = response_json["positions"]

    return position_orders


def get_current_position_order_by_symbol(symbol: str, api_key: str, secret_key: str):

    position_orders = get_current_position_orders(
        api_key=api_key, secret_key=secret_key
    )

    symbol_position_order = extract_current_position_order_by_symbol(
        position_orders=position_orders, symbol=symbol
    )

    return symbol_position_order
