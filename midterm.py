import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

names = ['temp', 'dpTemp' ,'RH', 'WDIR', 'VIZ']
df = pd.read_csv('./oversampler.csv', names=names)
array = df.values
x = array[:,1:4]
y = array[:,4]
seed = 7
kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)

lr = LinearRegression()
rr = Ridge()
las = Lasso()
el = ElasticNet()
knr = KNeighborsRegressor()
dt = DecisionTreeRegressor()
svr = SVR()

ests = {'LinearRegression':lr,'Ridge': rr,'Lasso': las, 'ElasticNet': el, 'KNeighborsRegressor': knr, 'DecisionTreeRegressor': dt, 'SVR': svr}

for est in ests:
    model = ests[est]
    scoring = 'neg_mean_squared_error'
    results = model_selection.cross_val_score(model, x, y, cv = kfold, scoring = scoring)
    print("{} : {}".format(est, results.mean()))