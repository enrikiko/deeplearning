from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

sc = MinMaxScaler(feature_range=(0, 1))
data_set_training = pd.read_csv("Google_Stock_Price_Train.csv")
training_set = data_set_training.iloc[:, 1:2].values
# print(training_set)
training_set_scaled = sc.fit_transform(training_set)
# print(training_set_scaled)
x_train = []
y_train = []
for i in range(60, 1258):
    x_train.append(training_set_scaled[i - 60:i, 0])
    y_train.append(training_set_scaled[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# Reshaping
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Initialising the RNN
regressor = Sequential()
# First layer
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
regressor.add(Dropout(rate=0.2))
# Second layer
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(rate=0.2))
# Third layer
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(rate=0.2))
# Last layer
regressor.add(LSTM(units=50))
regressor.add(Dropout(rate=0.2))

regressor.add(Dense(units=1))

regressor.compile(optimizer="adam", loss="mean_squared_error")

regressor.fit(x_train, y_train, epochs=100, batch_size=32)

data_set_test = pd.read_csv("Google_Stock_Price_Test.csv")
real_stock_price = data_set_test.iloc[:, 1:2].values

data_set_total = pd.concat((data_set_training["open"], data_set_test["open"]), axis=0)
inputs = data_set_total[len(data_set_total) - len(data_set_test) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)

x_test = []
for i in range(60, 80):
    x_test.append(inputs[i - 60:i, 0])


x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predicted_stock_price = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
print(predicted_stock_price)
# app = Flask(__name__)
#
# @app.route('/example/')
# def example():
#     return {'hello': 'world'}
#
# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0')
