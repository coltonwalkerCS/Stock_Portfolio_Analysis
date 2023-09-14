import yfinance as yf
import pandas as pd
import numpy as np
import quandl


def importAssetData():
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
    # Import AAPL
    aapl = yf.Ticker("AAPL")
    aapl_data = aapl.history(period="1y")
    print(aapl_data.head())

    # Import MSFT
    msft = yf.Ticker("MSFT")
    msft_data = msft.history(period="1y")
    print(msft_data.head())

    # Import EEM
    eem = yf.Ticker("EEM")
    eem_data = eem.history(period="1y")
    print(eem_data.head())

    # Import IEF
    ief = yf.Ticker("IEF")
    ief_data = ief.history(period="1y")

    # Import LQD
    lqd = yf.Ticker("LQD")
    lqd_data = lqd.history(period="1y")

    # Import VNQ
    vnq = yf.Ticker("VNQ")
    vnq_data = vnq.history(period="1y")

    # Import GLD
    gld = yf.Ticker("GLD")
    gld_data = gld.history(period="1y")

    # Import HYG
    hyg = yf.Ticker("HYG")
    hyg_data = hyg.history(period="1y")

    # Import TIP
    tip = yf.Ticker("TIP")
    tip_data = tip.history(period="1y")

    # Import MUB
    mub = yf.Ticker("MUB")
    mub_data = mub.history(period="1y")


importAssetData()