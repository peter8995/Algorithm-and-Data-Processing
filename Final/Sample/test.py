"""
https://autokeras.com/tutorial/timeseries_forecaster/
"""

import pandas as pd
import tensorflow as tf
import absl.logging
import autokeras as ak

absl.logging.set_verbosity(absl.logging.ERROR)

dataset = pd.read_csv('./AirQualityUCI.csv', sep=";")
dataset = dataset[dataset.columns[:-2]]     # 到倒數第二個(含)
dataset = dataset.dropna()      # 有空白就全部Drop
dataset = dataset.replace(",", ".", regex=True)     #用.取代,

val_split = int(len(dataset) * 0.7)
data_train = dataset[:val_split]
validation_data = dataset[val_split:]

data_x = data_train[
    [
        "CO(GT)",
        "PT08.S1(CO)",
        "NMHC(GT)",
        "C6H6(GT)",
        "PT08.S2(NMHC)",
        "NOx(GT)",
        "PT08.S3(NOx)",
        "NO2(GT)",
        "PT08.S4(NO2)",
        "PT08.S5(O3)",
        "T",
        "RH",
    ]
].astype("float64")

data_x_val = validation_data[
    [
        "CO(GT)",
        "PT08.S1(CO)",
        "NMHC(GT)",
        "C6H6(GT)",
        "PT08.S2(NMHC)",
        "NOx(GT)",
        "PT08.S3(NOx)",
        "NO2(GT)",
        "PT08.S4(NO2)",
        "PT08.S5(O3)",
        "T",
        "RH",
    ]
].astype("float64")

# Data with train data and the unseen data from subsequent time steps.
data_x_test = dataset[
    [
        "CO(GT)",
        "PT08.S1(CO)",
        "NMHC(GT)",
        "C6H6(GT)",
        "PT08.S2(NMHC)",
        "NOx(GT)",
        "PT08.S3(NOx)",
        "NO2(GT)",
        "PT08.S4(NO2)",
        "PT08.S5(O3)",
        "T",
        "RH",
    ]
].astype("float64")

data_y = data_train["AH"].astype("float64")

data_y_val = validation_data["AH"].astype("float64")

print(data_x.shape)  # (6549, 12)
print(data_y.shape)  # (6549,)

predict_from = 1
predict_until = 10
lookback = 32
clf = ak.TimeseriesForecaster(
    lookback=lookback,
    predict_from=predict_from,
    predict_until=predict_until,
    max_trials=1,
    objective="val_loss",
)
# Train the TimeSeriesForecaster with train data
clf.fit(
    x=data_x,
    y=data_y,
    validation_data=(data_x_val, data_y_val),
    batch_size=32,
    epochs=10,
)
# Predict with the best model(includes original training data).
predictions = clf.predict(data_x_test)
print(predictions.shape)
# Evaluate the best model with testing data.
print(clf.evaluate(data_x_val, data_y_val))
