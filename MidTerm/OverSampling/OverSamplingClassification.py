from numpy import asarray
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from autokeras import StructuredDataClassifier
from keras import callbacks

# load dataset
names = ['temp', 'dpTemp' ,'RH', 'WDIR', 'VIZ', 'Label']
dataframe = read_csv('./oversampler.csv', names=names)
print(dataframe.shape)

# split into input and output elements
data = dataframe.values
x = data[:,0:4]
y = data[:,5]
print(x.shape, y.shape)

# basic data preparation
x = x.astype('float32')
#y = LabelEncoder().fit_transform(y)

# separate into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# define the search
search = StructuredDataClassifier(max_trials=100, overwrite=True)

# perform the early stopping
earlystopping = callbacks.EarlyStopping(monitor ="val_loss", 
                                        mode ="min", patience = 5, 
                                        restore_best_weights = True)

# perform the search
search.fit(x=X_train, y=y_train, callbacks=[earlystopping] ,verbose=2)

# evaluate the model
loss, acc = search.evaluate(X_test, y_test, verbose=1)
print('Accuracy: %.3f' % acc)

# use the model to make a prediction
row = [15.1,14.9,99,50]
X_new = asarray([row]).astype('float32')
yhat = search.predict(X_new)
print('Predicted: %.3f' % yhat[0])

# get the best performing model
model = search.export_model()

# summarize the loaded model
model.summary()

# save the best performing model to filetry:
try:
    model.save("modelOverSampling", save_format="tf")
except Exception:
    model.save("modelOverSampling.h5")