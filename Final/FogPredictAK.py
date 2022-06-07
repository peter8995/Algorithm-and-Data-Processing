import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import autokeras as ak
import absl.logging
from sklearn.metrics import mean_squared_error, mean_absolute_error

log_dir='.\\logs'
absl.logging.set_verbosity(absl.logging.ERROR)
#tf.debugging.experimental.enable_dump_debug_info(log_dir, tensor_debug_mode="FULL_HEALTH", circular_buffer_size=-1)

dataset = pd.read_csv('./Fog.csv')
"""
dataset = dataset.replace("X", NULL)
dataset = dataset.replace("V", NULL)
dataset = dataset.dropna()
"""
dataset.drop(dataset.index[dataset[(dataset.values == 'X') | \
    (dataset.values == 'V')].index], inplace=True)
dataset = dataset.drop(['time','Label'],axis=1)
dataset = dataset.astype("float64")
dataset
dataset.info()

fig = plt.figure(figsize=(10, 12))

names = ('VIZ', 'temp', 'dpTemp', 'RH', 'WDIR')

for i in range(5):
    data = dataset[names[i]]
    ax = fig.add_subplot(5, 1, i + 1)
    plt.scatter(np.arange(data.size), data, s=1)
    ax.set_xlim([0, data.size])
    ax.set_title(names[i])

plt.tight_layout()
plt.show()

split = 0.125

x = dataset.drop(['VIZ'], axis=1)
y = dataset['VIZ']

slice_index = int(y.size * (1 - split))
x_train, x_test = x[:slice_index], x[slice_index:]
y_train, y_test = y[:slice_index], y[slice_index:]

x_train.info()
x_test.info()
print(x_train.shape)
print(x_test.shape)

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

lookback = 72
batch_size = 24

fog = ak.TimeseriesForecaster(
    lookback=lookback, max_trials=100)

fog.fit(
    x_train, y_train, batch_size=batch_size,epochs=3
    )

predicted= fog.predict(x).flatten()
real = y_test[lookback:]

print('Prediction MSE:', mean_squared_error(real, predicted).round(3))
print('Prediction MAE:', mean_absolute_error(real, predicted).round(3))

display_size = 250

dx = np.arange(predicted.size)

plt.figure(figsize=(10, 6))
plt.title('Predictions')
plt.plot(dx[:display_size], predicted[:display_size],
         linestyle='--', linewidth=3, label='Predicted')
plt.xlim([0, display_size])
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.title('Predictions')
plt.plot(dx[:display_size], real[:display_size],linewidth=2, label='Real')
plt.plot(dx[:display_size], predicted[:display_size],
         linestyle='--', linewidth=3, label='Predicted')
plt.xlim([0, display_size])
plt.legend()
plt.tight_layout()
plt.show()