from . import _indicators
from automated_trading.constants import PositionAction
import pandas as pd
from typing import Literal


def apply_cdc_strategy(
    df: pd.DataFrame,
) -> Literal[
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

    df["action"] = df.apply(
        lambda row: (
            None
            if pd.isna(row["EMA_12"])
            else _apply_cdc_logic(row["is_fast_cross"], row["is_shifted_fast_cross"])
        ),
        axis=1,
    )

    action = df.loc[df.shape[0] - 2, "action"]
    return action
