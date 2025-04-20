import pandas_ta as ta

cdc_strategy = ta.Strategy(
    name="cdc strategy",
    description="ema 12 crossing ema 26",
    ta=[
        {"kind": "ema", "length": 12},
        {"kind": "ema", "length": 26},
    ],
)
