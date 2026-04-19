#Basic Accuracy Example

from sklearn.metrics import accuracy_score

y_true = [1,0,1,1,0]
y_pred = [1,0,1,0,0]

acc = accuracy_score(y_true, y_pred)
print(acc)

#Iris Dataset Accuracy

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))


#Pass / Fail Accuracy

y_true = [1,1,0,1,0]
y_pred = [1,0,0,1,0]

print(accuracy_score(y_true, y_pred))

#Digits Dataset Accuracy

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

digits = load_digits()

X_train,X_test,y_train,y_test = train_test_split(
    digits.data,digits.target,test_size=0.2,random_state=1)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print(accuracy_score(y_test,pred))

#Compare Algorithms Accuracy

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
print("KNN:", knn.score(X_test,y_test))

svm = SVC()
svm.fit(X_train,y_train)
print("SVM:", svm.score(X_test,y_test))

#Basic RMSE Example
from sklearn.metrics import mean_squared_error
import numpy as np

y_true = [50,60,70]
y_pred = [55,58,72]

rmse = np.sqrt(mean_squared_error(y_true,y_pred))
print(rmse)

#Exam Score Prediction
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [40,50,60,70,80]

model = LinearRegression()
model.fit(X,y)

pred = model.predict(X)

rmse = np.sqrt(mean_squared_error(y,pred))
print(rmse)

#Salary Prediction RMSE
X = [[1],[2],[3],[4],[5]]
y = [20000,30000,40000,50000,60000]

model.fit(X,y)
pred = model.predict(X)

print(np.sqrt(mean_squared_error(y,pred)))

#House Price Example
actual = [200,250,300,350]
pred   = [210,245,295,360]

print(np.sqrt(mean_squared_error(actual,pred)))

#Compare Two Regression Models
pred1 = [52,62,69]
pred2 = [48,61,75]
true  = [50,60,70]

rmse1 = np.sqrt(mean_squared_error(true,pred1))
rmse2 = np.sqrt(mean_squared_error(true,pred2))

print("Model 1:", rmse1)
print("Model 2:", rmse2)