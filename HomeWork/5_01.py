import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

data=pd.read_csv('data.csv')
print(data.head(5))
print(data.describe())
print(data.groupby('species').size())

#Holdout split
train, test = train_test_split (data, test_size=0.4, stratify=data['species'], random_state=42)

n_bins = 10
fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(train ['sepal_length'], bins=n_bins)
axs[0, 0].set_title('Sepal Length')
axs[0, 1].hist(train['sepal_width'], bins=n_bins)
axs[0, 1].set_title('Sepal Width')
axs[1, 0].hist(train['petal_length'], bins=n_bins)
axs[1, 0].set_title('Petal Length')
axs[1, 1].hist(train['petal_width'], bins=n_bins)
axs[1, 1].set_title('Petal Width')

# add some spacing between subplots
fig.tight_layout(pad=1.0)
fig.show()

X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
y_train = train.species
X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
y_test = test.species

mod_dt = DecisionTreeClassifier(max_depth=3,random_state=1)
mod_dt.fit(X_train,y_train)
prediction = mod_dt.predict(X_test)
print('The accuracy of the Decision Tree is',"{:.3f}".format(metrics.accuracy_score(prediction, y_test)))
fn = ['sepal_length','sepal_width','petal_length','petal_width']
cn = ['setosa','versicolor','virginica']

plt.figure(figsize=(10,8))
plot_tree(mod_dt,feature_names=fn,class_names=cn,filled=True)
plt.show()


mod_dt = KNeighborsClassifier()
mod_dt.fit(X_train, y_train)
prediction = mod_dt.predict(X_test)
print('The accuracy of the KNN is', "{:.3f}".format(metrics.accuracy_score(prediction, y_test)))

mod_dt = SVC()
mod_dt.fit(X_train, y_train)
prediction = mod_dt.predict(X_test)
print('The accuracy of the SVC is', "{:.3f}".format(metrics.accuracy_score(prediction, y_test)))

##GaussianNB
mod_dt = GaussianNB()
mod_dt.fit(X_train, y_train)
prediction = mod_dt.predict(X_test)
print('The acccuracy of the GaussianNB is', "{:.3f}".format(metrics.accuracy_score(prediction, y_test)))