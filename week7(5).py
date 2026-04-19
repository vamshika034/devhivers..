#Student Scores Prediction
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [35,45,55,65,75]

model = LinearRegression()
model.fit(X,y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

print("Prediction for 6 hours:", model.predict([[6]]))

#Plot Regression Line
import matplotlib.pyplot as plt

plt.scatter(X,y)

plt.plot(X, model.predict(X))

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

#House Price Prediction
X = [[500],[700],[900],[1100],[1300]]
y = [10,15,20,25,30]   # in lakhs

model = LinearRegression()
model.fit(X,y)

print(model.predict([[1000]]))

#Salary Prediction
X = [[1],[2],[3],[4],[5]]
y = [20000,30000,40000,50000,60000]

model.fit(X,y)

print(model.predict([[6]])


#Temperature Prediction
X = [[1],[2],[3],[4],[5]]
y = [22,24,26,28,30]

model.fit(X,y)

print(model.predict([[6]]))


#Example (Negative Slope)
X = [[20],[40],[60],[80]]
y = [60,40,30,20]

model.fit(X,y)
print(model.coef_)
