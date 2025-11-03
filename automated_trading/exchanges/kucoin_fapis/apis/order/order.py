from automated_trading.exchanges.kucoin_fapis.apis.base_api import BaseFutureApi
from automated_trading.utils import generate_uuid
from aiohttp import ClientSession
from . import _model
from typing import Literal


class OrderApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    async def aplace_order(
        self,
        session: ClientSession,
        client_id: str,
        symbol: str,
        side: Literal["buy", "sell"],
        type: Literal["market", "limit"],
        price: str = "",
        qty: str = "",
        value_qty: str = "",
        margin_model: Literal["ISOLATED", "CROSS"] = "CROSS",
        leverage: int = 125,
        is_test: bool = False,
    ):
        if is_test:
            model = _model.PostCreateOrderTest()
        else:
            model = _model.PostCreateOrder()

        data = {
            "clientOid": client_id,
            "side": side,
            "symbol": symbol,
            "type": type,
            "price": price,
            "qty": qty,
            "leverage": leverage,
            "valueQty": value_qty,
            "marginMode": margin_model,
        }

        payload = self.prepare_post_payload(endpoint=model.endpoint, data=data)
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result["data"]

    async def aplace_st_order(
        self,
        session: ClientSession,
        client_id: str,
        symbol: str,
        side: Literal["buy", "sell"],
        type: Literal["market", "limit"],
        price: str = "",
        qty: str = "",
        value_qty: str = "",
        trigger_stop_up_price: str = "",
        trigger_stop_down_price: str = "",
        margin_model: Literal["ISOLATED", "CROSS"] = "CROSS",
        stopPriceType: str = "TP",
        leverage: int = 125,
    ):
        model = _model.PostCreateStOrder()
        data = {
            "clientOid": client_id,
            "side": side,
            "symbol": symbol,
            "type": type,
            "price": price,
            "qty": qty,
            "leverage": leverage,
            "valueQty": value_qty,
            "marginMode": margin_model,
            "triggerStopUpPrice": trigger_stop_up_price,
            "triggerStopDownPrice": trigger_stop_down_price,
            "stopPriceType": stopPriceType,
        }

        payload = self.prepare_post_payload(endpoint=model.endpoint, data=data)
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result

    async def aget_order_list(
        self,
        session: ClientSession,
        symbol: str,
        status: Literal["active", "done"] = "active",
        side: Literal["buy", "sell"] = None,
        type: Literal["limit", "market"] = None,
    ):
        model = _model.GetOrderList()
        query_params = {
            "symbol": symbol,
            "status": status,
        }
        if side is not None:
            query_params |= {"side": side}
        if type is not None:
            query_params |= {"type": type}

        payload = self.prepare_get_payload(
            endpoint=model.endpoint, query_params=query_params
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result

    async def aclose_order(self, session: ClientSession, client_id: str, symbol: str):
        model = _model.PostCreateOrder()

        data = {
            "clientOid": client_id,
            "symbol": symbol,
            "closeOrder": True,
            "type": "market",
            "marginMode": "CROSS",
        }

        payload = self.prepare_post_payload(endpoint=model.endpoint, data=data)
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result
