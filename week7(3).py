#Basic Split Example
from sklearn.model_selection import train_test_split

X = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [2,4,6,8,10,12,14,16]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

print("Train:", X_train)
print("Test:", X_test)

#Student Scores Regression
#Predict Marks from Study Hours
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5],[6]]
y = [35,45,55,65,75,85]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.predict(X_test))
print("Test Score:", model.score(X_test, y_test))

#Compare Train Accuracy vs Test Accuracy
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy :", model.score(X_test, y_test))

#Iris Dataset Classification Split

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

#Compare Different Splits

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

for size in [0.2, 0.3, 0.4]:
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=size, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    print("Test Size:", size, "Accuracy:", model.score(X_test, y_test))