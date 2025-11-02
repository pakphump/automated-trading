import pandas_ta as ta

cdc_indicators = ta.Study(
    name="CDC Strategy",
    description="CDC Strategy using EMA 12,26 Crossing",
    cores=0,
    ta=[
        {"kind": "ema", "length": 12},
        {"kind": "ema", "length": 26},
    ],
)
