from urllib.parse import urlencode
import hashlib
import hmac


def create_signature(secret_key: str, payload: dict):
    signature = hmac.new(
        secret_key.encode("utf-8"),
        urlencode(payload).encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return signature


def add_signature_in_payload(secret_key: str, payload: dict):
    signature = create_signature(secret_key, payload)
    payload["signature"] = signature

    return payload
