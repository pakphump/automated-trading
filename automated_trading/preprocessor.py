import pandas as pd
from automated_trading.constants import KLINE_COLUMNS
from typing import List


def preprocess_klines_data(kline_list: list) -> pd.DataFrame:

    kline_df = pd.DataFrame(kline_list)
    kline_df.columns = KLINE_COLUMNS

    # Prep Time
    kline_df["time"] = pd.to_datetime(kline_df["time"], unit="ms")
    kline_df["close_time"] = pd.to_datetime(kline_df["close_time"], unit="ms")

    to_float_cols = ["open", "high", "low", "close", "volume"]
    kline_df[to_float_cols] = kline_df[to_float_cols].astype(float)

    return kline_df


def extract_current_position_order_by_symbol(position_orders: List[dict], symbol: str):
    for order in position_orders:
        if order["symbol"] == symbol:
            return order

    return None
