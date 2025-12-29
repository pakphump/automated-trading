from . import _indicators
from automated_trading.constants import PositionAction
import pandas as pd
from typing import Literal


def apply_cdc_strategy(df: pd.DataFrame, atr_multiplier: float) -> Literal[
    PositionAction.OPEN_LONG,
    PositionAction.OPEN_SHORT,
    PositionAction.HOLD_LONG,
    PositionAction.HOLD_SHORT,
]:

    def _apply_cdc_logic(fast_cross, fast_cross_shift):
        if fast_cross != fast_cross_shift:
            open_side = (
                PositionAction.OPEN_LONG if fast_cross else PositionAction.OPEN_SHORT
            )
            return open_side.value

        else:
            hold_side = (
                PositionAction.HOLD_LONG if fast_cross else PositionAction.HOLD_SHORT
            )
            return hold_side.value

    df.ta.study(_indicators.cdc_indicators)
    df["is_fast_cross"] = df["EMA_12"] > df["EMA_26"]
    df["is_shifted_fast_cross"] = df["is_fast_cross"].shift(1)
    df["atr_upper"] = df["high"] + df["ATRr_14"] * atr_multiplier
    df["atr_lower"] = df["low"] + df["ATRr_14"] * atr_multiplier

    df["action"] = df.apply(
        lambda row: (
            None
            if pd.isna(row["EMA_12"])
            else _apply_cdc_logic(row["is_fast_cross"], row["is_shifted_fast_cross"])
        ),
        axis=1,
    )

    action = df.loc[df.shape[0] - 2, "action"]

    current_price = float(df.loc[df.shape[0] - 1, "close"])
    stoploss_price = None

    if action == "open_long":
        stoploss_price = df.loc[df.shape[0] - 1, "atr_lower"]
    elif action == "open_short":
        stoploss_price = df.loc[df.shape[0] - 1, "atr_upper"]

    return action, current_price, stoploss_price
