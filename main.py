from GatherHistoricalData import importAssetData, importAssetDataSingle, createCorrelationMatrix
from RegressionAnalysis import predict_stock_price
import numpy as np

""" SIMPLE Asset_ID's, can be more complex in a more complex system"""
weights = {'1': 0.15, '2': 0.15, '3': 0.1, '4': 0.1,  '5': 0.12,
           '6': 0.13, '7': 0.06, '8': 0.07,  '9': 0.07,  '10': 0.05}

portfolio_id_ticker_list = [('1', "AAPL"), ('2', "MSFT"), ('3', "EEM"), ('4', "IEF"),  ('5', "LQD"),
                            ('6', "VNQ"), ('7', "GLD"), ('8', "HYG"),  ('9', "TIP"),  ('10', "MUB")]

historical_asset_data_db = importAssetData(portfolio_id_ticker_list, "3y", interval="1d")
# Sample start date
start_date = '2023-09-11 00:00:00-04:00'

corrMatrix = createCorrelationMatrix(historical_asset_data_db, portfolio_id_ticker_list)
# print(historical_asset_data_db["1"].tail())
# print(historical_asset_data_db["1"].loc['2022-09-12 00:00:00-04:00']['Open'])

"""TEST Regression Analysis"""
print("DATA")
predict_stock_price(historical_asset_data_db, '1')


"""
-- ASSET FULL LIST --
-US Stock: Apple Inc. (AAPL)
-International Stock: Microsoft Corporation (MSFT)
-Emerging Markets Stock: iShares MSCI Emerging Markets ETF (EEM)
-US Government Bond: iShares 7-10 Year Treasury Bond ETF (IEF)
-Corporate Bond:iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD)
-Real Estate Investment Trust (REIT): Vanguard Real Estate ETF (VNQ)
-Commodity: SPDR Gold Trust (GLD)
-High-Yield Bond: iShares iBoxx $ High Yield Corporate Bond ETF (HYG)
-US Treasury Inflation-Protected Security (TIPS): iShares TIPS Bond ETF (TIP)
-Municipal Bond: iShares National Muni Bond ETF (MUB)
"""
