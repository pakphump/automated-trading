import pandas_ta as ta
import pandas as pd
from typing import Literal

_setup_cdc_strategy = ta.Strategy(
    name="cdc strategy",
    description="ema 12 crossing ema 26",
    ta=[
        {"kind": "ema", "length": 12},
        {"kind": "ema", "length": 26},
    ],
)


def process_cdc_strategy(
    kline_df: pd.DataFrame,
) -> Literal["open_long", "open_short", "hold_long", "hold_short"]:

    def _apply_cdc_logic(fast_cross, fast_cross_shift):
        if fast_cross != fast_cross_shift:
            return "open_long" if fast_cross else "open_short"
        else:
            return "hold_long" if fast_cross else "hold_short"

    kline_df.ta.strategy(_setup_cdc_strategy)

    kline_df["is_fast_cross"] = kline_df["EMA_12"] > kline_df["EMA_26"]
    kline_df["is_shifted_fast_cross"] = kline_df["is_fast_cross"].shift(1)

    kline_df["action"] = kline_df.apply(
        lambda row: (
            None
            if pd.isna(row["EMA_12"])
            else _apply_cdc_logic(row["is_fast_cross"], row["is_shifted_fast_cross"])
        ),
        axis=1,
    )

    action = kline_df.loc[kline_df.shape[0] - 2, "action"]

    return action
