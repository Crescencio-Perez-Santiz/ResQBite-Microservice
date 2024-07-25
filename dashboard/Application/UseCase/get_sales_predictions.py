from Infrastructure.repositories.sales_repository import get_finalized_orders_by_store
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def get_sales_predictions(store_uuid):
    orders = get_finalized_orders_by_store(store_uuid)

    sales_data = pd.DataFrame(
        [{'date': order.created_at, 'quantity': order.total_price} for order in orders])
    sales_data['date'] = pd.to_datetime(sales_data['date'])
    sales_data.set_index('date', inplace=True)
    monthly_sales = sales_data.resample('MS').sum()

    real_data = [{'month': date.strftime('%Y-%m'), 'quantity': quantity}
                 for date, quantity in monthly_sales['quantity'].items()]

    prediction_data = []

    if len(monthly_sales) >= 24:
        model_hw = ExponentialSmoothing(
            monthly_sales['quantity'], seasonal='add', seasonal_periods=12).fit()
        hw_forecast = model_hw.forecast(steps=3)
        for i, quantity in enumerate(hw_forecast):
            prediction_data.append({
                'month': (monthly_sales.index[-1] + pd.DateOffset(months=i+1)).strftime('%Y-%m'),
                'quantity': float(quantity)
            })

    # Preparar datos para RNN
    rnn_data = monthly_sales['quantity'].values
    rnn_data = rnn_data.reshape(-1, 1)

    def create_sequences(data, seq_length):
        xs, ys = [], []
        for i in range(len(data)-seq_length):
            x = data[i:i+seq_length]
            y = data[i+seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)

    seq_length = 3
    if len(rnn_data) > seq_length:
        X, y = create_sequences(rnn_data, seq_length)

        model_rnn = Sequential()
        model_rnn.add(LSTM(50, activation='relu', input_shape=(seq_length, 1)))
        model_rnn.add(Dense(1))
        model_rnn.compile(optimizer='adam', loss='mse')
        model_rnn.fit(X, y, epochs=200, verbose=0)

        rnn_input = rnn_data[-seq_length:].reshape((1, seq_length, 1))
        for _ in range(3):
            pred = model_rnn.predict(rnn_input)
            prediction_data.append({
                'month': (monthly_sales.index[-1] + pd.DateOffset(months=len(prediction_data)+1)).strftime('%Y-%m'),
                'quantity': float(pred[0, 0])
            })
            rnn_input = np.append(
                rnn_input[:, 1:, :], pred.reshape(1, 1, 1), axis=1)

    return {
        'real_data': real_data,
        'prediction': prediction_data
    }
