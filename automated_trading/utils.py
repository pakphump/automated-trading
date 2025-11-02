from urllib.parse import urlencode
import hashlib
import hmac
import datetime


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


def get_current_utc_timestamp_ms() -> int:
    return int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)


def calculate_start_klines(n_row: int, timeframe: int, end: int):
    interval_ms = timeframe * 60 * 1000
    start = end - (n_row * interval_ms)
    return start


from typing import List, Tuple


def split_klines_requests(
    n_records: int,
    timeframe: int,
    end: int,
    max_records_per_request: int = 200,
) -> List[Tuple[int, int]]:

    interval_ms = timeframe * 60 * 1000

    requests = []
    remaining = n_records
    current_end = end

    while remaining > 0:
        # Number of records to fetch this chunk, max max_records_per_request
        count = min(remaining, max_records_per_request)

        # Calculate the start timestamp for this chunk
        current_start = current_end - (count * interval_ms)

        requests.append((current_start, current_end))

        # Update end for next chunk (one interval before current_start)
        # To avoid overlapping, next end is current_start - interval_ms
        current_end = current_start - interval_ms

        remaining -= count

    # Requests are built from newest chunk backward, so reverse to oldest->newest order
    return list(reversed(requests))
