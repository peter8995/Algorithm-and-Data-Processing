import pandas as pd
import tensorflow as tf
import autokeras as ak
import absl.logging
from keras import callbacks

log_dir='.\\logs'
absl.logging.set_verbosity(absl.logging.ERROR)
#tf.debugging.experimental.enable_dump_debug_info(log_dir, tensor_debug_mode="FULL_HEALTH", circular_buffer_size=-1)

dataset = pd.read_csv('./Fog1.csv')
"""
dataset = dataset.replace("X", NULL)
dataset = dataset.replace("V", NULL)
dataset = dataset.dropna()
"""
dataset.drop(dataset.index[dataset[(dataset.values == 'X') | \
    (dataset.values == 'V')].index], inplace=True)
#print(dataset)

val_split = int(len(dataset) * 0.7)
data_train = dataset[:val_split]
validation_data = dataset[val_split:]

data_x = data_train[
    [
        "temp",
        "dpTemp",
        "RH",
        "WDIR"
    ]
].astype("float64")

data_x_val = validation_data[
    [
        "temp",
        "dpTemp",
        "RH",
        "WDIR"
    ]
].astype("float64")

data_x_test = dataset[
    [
        "temp",
        "dpTemp",
        "RH",
        "WDIR"
    ]
].astype("float64")

data_y = data_train["VIZ"].astype("float64")

data_y_val = validation_data["VIZ"].astype("float64")

print(data_x.shape)
print(data_y.shape)
print(data_x_val.shape)
print(data_y_val.shape)
print(data_x_test.shape)

predict_from = 1    # default 每次加1
predict_until = 10
lookback = 23
Fog = ak.TimeseriesForecaster(
    lookback=lookback,
    predict_until = predict_until,
    objective="val_loss",
)

cllbs = [callbacks.EarlyStopping(monitor = "loss",
                                mode ="min",patience = 5,
                                restore_best_weights = True),
                                callbacks.TensorBoard(log_dir)]

Fog.fit(
    x = data_x, y = data_y,
    validation_data = (data_x_val, data_y_val),
    epochs = 100
)

predictions = Fog.predict(data_x_test)

print(predictions.shape)

print(Fog.evaluate(data_x_val, data_y_val))
