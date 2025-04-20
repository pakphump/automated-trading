from automated_trading.binance_apis.market_data import get_continuous_klines
from automated_trading.preprocessor import preprocess_klines_data
from automated_trading.strategies import process_cdc_strategy


class AutomatedTrading:
    def __init__(self):
        pass

    def run_cdc_strategy(self, symbol, interval):

        # Get Kline data
        kline_list = get_continuous_klines(symbol=symbol, interval=interval)
        kline_df = preprocess_klines_data(kline_list)

        cdc_action = process_cdc_strategy(kline_df)

        return cdc_action
