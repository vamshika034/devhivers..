#Load Iris Dataset

from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data[:5])      # first 5 rows
print(iris.target[:5])    # labels
print(iris.feature_names)
print(iris.target_names)


#Train Decision Tree Classifier

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

print("Training Complete")

#Predict Flower Type

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])

print(prediction)
print(iris.target_names[prediction])

#Check Accuracy using .score()
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.score(X, y))

#Digits Dataset Prediction

from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier

digits = load_digits()

X = digits.data
y = digits.target

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([X[0]]))
print("Actual:", y[0])

