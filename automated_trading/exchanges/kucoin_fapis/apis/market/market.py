from automated_trading.exchanges.kucoin_fapis.apis.base_api import BaseFutureApi
from automated_trading.constants import KUCOIN_KLINE_COLUMNS, KLINE_FLOAT_COLUMNS
from automated_trading import utils
from aiohttp import ClientSession
import asyncio
import pandas as pd
from . import _model


class MarketApi(BaseFutureApi):
    def __init__(self, api_key, api_secret, api_passphrase):
        super().__init__(api_key, api_secret, api_passphrase)

    @staticmethod
    def _prep_kline_df(data):
        df = pd.DataFrame(data, columns=KUCOIN_KLINE_COLUMNS)
        df["time"] = pd.to_datetime(df["time"], unit="ms")
        df[KLINE_FLOAT_COLUMNS] = df[KLINE_FLOAT_COLUMNS].astype(float)

        return df

    async def aget_symbol_info(self, session: ClientSession, symbol: str):
        model = _model.GetSymbol()

        payload = self.prepare_get_payload(
            endpoint=model.endpoint.format(symbol=symbol),
            query_params=b"",
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result["data"]

    async def aget_all_symbol_info(self, session: ClientSession):
        model = _model.GetAllSymbolActive()

        payload = self.prepare_get_payload(
            endpoint=model.endpoint,
            query_params=b"",
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        return result["data"]

    async def _aget_klines(
        self, session: ClientSession, symbol: str, timeframe: int, start: int, end: int
    ):
        model = _model.GetKlines()
        query_params = {
            "symbol": symbol,
            "granularity": timeframe,
            "from": start,
            "to": end,
        }
        payload = self.prepare_get_payload(
            endpoint=model.endpoint,
            query_params=query_params,
        )
        response = await session.request(**payload)
        response.raise_for_status()

        result = await response.json()
        df = self._prep_kline_df(result["data"])
        return df

    async def aget_klines(
        self,
        session: ClientSession,
        symbol: str,
        timeframe: int,
        n_records: int,
        end: int = None,
    ):
        record_chunks = utils.split_klines_requests(
            n_records=n_records, timeframe=timeframe, end=end
        )

        tasks = []
        for start_ts, end_ts in record_chunks:
            tasks.append(
                self._aget_klines(
                    session=session,
                    symbol=symbol,
                    timeframe=timeframe,
                    start=start_ts,
                    end=end_ts,
                )
            )
        result = await asyncio.gather(*tasks)
        df = pd.concat(result).drop_duplicates().reset_index(drop=True)
        return df
