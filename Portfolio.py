"""
This is the portfolio object, it contains:
the name of each stock, its weight, etc.
"""
from GatherHistoricalData import getAssetVolatility, getPurchaseInfo, createCorrelationMatrix
# TODO: Implement helper functions: getPrice(atDate),


class TransactionHistory:
    # TODO: Make list, or different D.S. that contains history of transactions
    def __init__(self, asset_ID, start_date, purchase_amount, quantity_shares):
        self.asset_ID = asset_ID
        self.start_date = start_date
        self.purchase_amount = purchase_amount
        self.quantity_shares = quantity_shares


class RiskMetrics:
    # TODO: Implement these risk metrics in future
    alpha = None
    beta = None
    sharp_ratio = None
    VaR = None
    CVaR = None
    liquidity_risk = None

    def __init__(self, asset_ID, annual_volatility):
        self.asset_ID = asset_ID
        self.annual_volatility = annual_volatility


class PortAsset:

    def __init__(self, asset_ID, name,  weight, annual_vol, purchase_price, quantity_shares, purchase_date):
        self.asset_ID = asset_ID
        self.asset_name = name
        self.asset_weight = weight
        self.asset_risk_metrics = RiskMetrics(asset_ID, annual_vol)
        self.purchase_price = purchase_price
        self.quantity_shares = quantity_shares
        self.purchase_date = purchase_date
        self.cost_basis = self.purchase_price * self.quantity_shares
        # self.asset_allocation TODO: FIGURE OUT WHAT THIS IS


    # def getCurrentMarketValue(self, current_date):
        # TODO: Function outside which given the name
        #        and date finds the current market price,
        #        should be universal (any stock can be a param)

    # def getCurrentMarketReturn(self, current_date):
        # TODO: GET RETURN BASED ON DATA


class Portfolio:
    correlation_matrix = []  # TODO: Implement function that reads in port_id_ticker_data and gens the corr matrix
    asset_collection = {}

    def __init__(self, portfolio_id_ticker, assets_historical_data, portfolio_id_weights, start_date, intitial_captial):
        self.portfolio_id_ticker = portfolio_id_ticker  # ID/Ticker list: [(ID, TICKER),...]
        self.assets_historical_data = assets_historical_data  # Hist Data dict: Key=asset_id, Item=pandas_df-hist_data
        self.portfolio_id_weights = portfolio_id_weights  # ID/Weights dict: Key=ID, Item=Weight | SUM(port_id_wght) = 1
        self.initial_capital = intitial_captial  # Starting amount of $ for investment portfolio
        self.start_date = start_date  # Start date of portfolio Y-M-D

        self.impl_port_assets_structure(assets_historical_data, portfolio_id_weights)

        self.correlation_matrix = createCorrelationMatrix(assets_historical_data, portfolio_id_ticker)

    def impl_port_assets_structure(self, assets_db, weights):
        """Initialize the individual assets within the portfolio"""
        for asset in self.portfolio_id_ticker:
            # Get the volume of a ticker given its historical data
            ticker_vol = getAssetVolatility(assets_db[asset[0]]["Close"].tolist())

            # Get the purchase price and number of shares for the asset
            purchase_price, num_shares = getPurchaseInfo(assets_db, asset[0], weights[asset[0]],
                                                         self.initial_capital, self.start_date)

            # Create the asset object
            new_asset = PortAsset(asset[0], asset[1], self.portfolio_id_weights[asset[0]],
                                  ticker_vol, purchase_price, num_shares, self.start_date)

            # Add asset to portfolio collection
            self.asset_collection[asset[0]] = new_asset
