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


def getPurchaseInfo(assets_db, asset_ID, weight, portfolio_initial_investment, current_date):
    amount_to_spend = portfolio_initial_investment * weight
    stock_cost_at_open = assets_db[asset_ID].loc[current_date]['Open']
    num_shares = amount_to_spend / stock_cost_at_open
    return stock_cost_at_open, num_shares


def getPriceChangeList(closing_prices):
    """Given a list of closing prices find the % change and put into a list"""
    percent_returns = []
    prev_price = closing_prices[0]
    for idx in range(1, len(closing_prices)):
        percent_change = ((closing_prices[idx] - prev_price) / prev_price) * 100
        percent_returns.append(percent_change)
        prev_price = closing_prices[idx]
    return percent_returns


def getAssetVolatility(closing_prices):
    """Given a list of closing prices (daily, weekly, mo, etc...) find the std dev (volatility)"""
    weekly_returns = getPriceChangeList(closing_prices)
    return np.std(weekly_returns)


def createCorrelationMatrix(historical_data, id_name_key):
    """Given a db with asset historical data pre-process and return a correlation matrix"""
    # Preprocessing - make a pandas df with each asset and their daily returns
    column_names = []
    closing_prices_lists = []
    for id_name in id_name_key:
        column_names.append(id_name[1])
        closing_prices_lists.append(getPriceChangeList(historical_data[id_name[0]]["Close"].tolist()))

    asset_closing_prices = pd.DataFrame()

    for i in range(0, len(column_names)):
        asset_closing_prices[column_names[0]] = closing_prices_lists[0]

    correlation_matrix = asset_closing_prices.corr()

    return correlation_matrix
