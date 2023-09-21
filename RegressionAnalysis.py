import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def predict_stock_price(historical_data_db, asset_id):
    # Get historical data of asset
    asset_data = historical_data_db[asset_id]

    features = np.arange(len(asset_data)).reshape(-1, 1)
    target = asset_data['Close']

    # Split the data into training and testing sets (e.g., 80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Create a linear regression model
    lin_model = LinearRegression()
    svr_model = SVR(kernel='rbf')

    # Train the model on the training data
    lin_model.fit(X_train, y_train)
    svr_model.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred_lin = lin_model.predict(X_test)
    y_pred_svr = svr_model.predict(X_test)

    # Get last date
    # end_date = asset_data.index.tolist()
    # endDate = end_date[0].strftime('%Y-%m-%d')

    plt.figure(figsize=(12, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.plot(X_test, y_pred_lin, color='red', linewidth=2, label='Lin')
    plt.scatter(X_test, y_pred_svr, color='green', linewidth=2, label='Lin')
    plt.title('Linear Regression - Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()

    # Assuming 'asset_data' has a date index
    end_date = asset_data.index[-1]

    # Create a date range for the next year
    future_date_range = pd.date_range(end_date + pd.DateOffset(days=1), periods=365)

    # Convert the date range into features
    X_future = np.arange(len(asset_data), len(asset_data) + len(future_date_range)).reshape(-1, 1)

    # Make predictions for the future data
    y_pred_future_lin = lin_model.predict(X_future)
    y_pred_future_svr = svr_model.predict(X_future)

    # Plot actual, historical, and predicted prices
    plt.figure(figsize=(12, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual (Test Data)')
    plt.plot(X_future, y_pred_future_lin, color='red', linewidth=2, label='Linear (Future Prediction)')
    plt.scatter(X_future, y_pred_future_svr, color='green', linewidth=2, label='SVR (Future Prediction)')
    plt.title('SVR - Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()