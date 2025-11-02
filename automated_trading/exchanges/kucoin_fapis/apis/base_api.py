import hmac
import base64
import hashlib
import time
import json
from automated_trading.constants import KUCOIN_FUTURE_BASE_URI, ApiMethod
from urllib.parse import urlencode


class BaseFutureApi:
    def __init__(self, api_key: str, api_secret: str, api_passphrase: str):

        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase

        if api_passphrase and api_secret:
            self.api_passphrase = self._sign(
                plain=api_passphrase.encode("utf-8"),
                key=api_secret.encode("utf-8"),
            )

    def _sign(self, plain: bytes, key: bytes) -> str:
        hm = hmac.new(key, plain, hashlib.sha256)
        return base64.b64encode(hm.digest()).decode()

    def _headers(self, plain: str):
        timestamp = str(int(time.time() * 1000))
        signature = self._sign(
            plain=(timestamp + plain).encode("utf-8"),
            key=self.api_secret.encode("utf-8"),
        )

        return {
            "KC-API-KEY": self.api_key,
            "KC-API-PASSPHRASE": self.api_passphrase,
            "KC-API-TIMESTAMP": timestamp,
            "KC-API-SIGN": signature,
            "KC-API-KEY-VERSION": "2",
        }

    def _process_headers(self, body: bytes, raw_url: str, method: str):
        payload = method + raw_url + body.decode()
        headers = self._headers(payload)
        headers |= {"Content-Type": "application/json"}

        return headers

    def prepare_get_payload(self, endpoint: str, query_params: dict):
        full_endpoint = f"{endpoint}?{urlencode(query_params)}"
        method = ApiMethod.GET.value

        payload = {
            "method": method,
            "url": f"{KUCOIN_FUTURE_BASE_URI}{full_endpoint}",
            "headers": self._process_headers(
                body=b"", raw_url=full_endpoint, method=method
            ),
        }
        return payload

    def prepare_post_payload(self, endpoint: str, data: dict):
        body = json.dumps(data)
        method = ApiMethod.POST.value

        payload = {
            "method": method,
            "url": f"{KUCOIN_FUTURE_BASE_URI}{endpoint}",
            "data": data,
            "headers": self._process_headers(
                body=body.encode(), raw_url=endpoint, method=method
            ),
        }

        return payload
