import yfinance as yf
import pandas as pd
import numpy as np
import quandl
import logging
import warnings

""" Suppress new pandas warning **FutureWarning: Series.__getitem__ treating keys as positions is deprecated.** """
warnings.simplefilter(action="ignore", category=FutureWarning)

# class HistoricalDataDB:
#     # Dictionary of pandas df
#
#     def __init__(self, asset_list):
#


def importAssetDataSingle(ticker_symbol, period, interval):
    """ Given a ticker symbol and time frame (1y, 1mo...) return historical data"""
    # Supported intervals:  [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    try:
        ticker_import = yf.Ticker(ticker_symbol)
        ticker_hist_data = ticker_import.history(period=period, interval=interval)
        return ticker_hist_data
    except Exception as ex:
        logging.error(f" Error as {ex}")


def importAssetData(tickers, period, interval):
    """Given tickers (asset_ID, ticker), period and interval return a dictionary of historical data"""
    ticker_data_dict = {}
    for ticker in tickers:
        ticker_data_dict[ticker[0]] = importAssetDataSingle(ticker[1], period, interval)
    return ticker_data_dict

def preProcessingFuncs():
    # TODO: IMPLEMENT std dev (volatility)
    return 1