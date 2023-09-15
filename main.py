from GatherHistoricalData import importAssetData, importAssetDataSingle
# Test importing df into dictionary

""" SIMPLE Asset_ID's, can be more complex in a more complex system"""
# weights = [0.15, 0.15, 0.1, 0.1, 0.12, 0.13, .06, .07, 0.07, 0.05]
portfolio_id_ticker_list = [('1', "AAPL"), ('2', "MSFT"), ('3', "EEM"), ('4', "IEF"),  ('5', "LQD"),  ('6', "VNQ"), ('7', "GLD"),
                       ('8', "HYG"),  ('9', "TIP"),  ('10', "MUB")]

historical_asset_data_db = importAssetData(portfolio_id_ticker_list, "1y", interval="1wk")

# for key in test_db:
#     print("Key: ")
#     print(test_db[key].head())


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
