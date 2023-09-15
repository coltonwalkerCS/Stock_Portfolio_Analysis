"""
This is the portfolio object, it contains:
the name of each stock, its weight, etc.
"""

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
    correlation_matrix = [] # TODO: Implement function that reads in port_id_ticker_data and gens the corr matrix

    def __init__(self, portfolio_id_ticker, assets_historical_data, portfolio_id_weights):
        self.portfolio_id_ticker = portfolio_id_ticker  # ID/Ticker list: [(ID, TICKER),...]
        self.assets_historical_data = assets_historical_data  # Hist Data dict: Key=asset_id, Item=pandas_df-hist_data
        self.portfolio_id_weights = portfolio_id_weights  # ID/Weights dict: Key=ID, Item=Weight | SUM(port_id_wght) = 1
        # for id_tick in id_ticker_list:

    def impl_port_assets_structure(self):
        for asset in self.portfolio_id_ticker:
            # TODO: Vol, purchase_price, quantity_shares, purchase_date need to be implemented
            # TODO: Quantity_shares can be calc by port_value * asset weight
            new_asset = PortAsset(asset[0], asset[1], self.portfolio_id_weights[asset[0]], 0.15, 100, 50, "Feb 12, 2023")

