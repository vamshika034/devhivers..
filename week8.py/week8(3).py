# Example 1: Predict Exam Scores using Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Study hours
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Exam scores
y = np.array([35, 42, 55, 70, 82, 90])

# Convert to polynomial features (degree=2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)

# Predict score for 7 hours
new_data = poly.transform([[7]])
print("Predicted Score:", model.predict(new_data)[0])

# Plot curve
X_range = np.linspace(1, 7, 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)

plt.scatter(X, y, color="blue")
plt.plot(X_range, model.predict(X_range_poly), color="red")
plt.title("Polynomial Regression - Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()

# Example 2: Compare Linear vs Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
y = np.array([10, 18, 28, 45, 65, 90])

# Linear model
linear = LinearRegression()
linear.fit(X, y)

# Polynomial model
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Plot
plt.scatter(X, y, color="black")

plt.plot(X, linear.predict(X), color="green", label="Linear Fit")

X_range = np.linspace(1,6,100).reshape(-1,1)
plt.plot(X_range, poly_model.predict(poly.transform(X_range)),
         color="red", label="Polynomial Fit")

plt.title("Linear vs Polynomial")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


# Example 3: Predict House Prices using Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# House size in sq ft
X = np.array([500, 700, 900, 1100, 1300, 1500]).reshape(-1,1)

# Prices in Lakhs
y = np.array([20, 28, 40, 58, 80, 110])

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Predict price for 1400 sq ft
new_house = poly.transform([[1400]])
print("Predicted Price:", model.predict(new_house)[0], "Lakhs")

# Plot
X_range = np.linspace(500,1500,100).reshape(-1,1)

plt.scatter(X, y, color="blue")
plt.plot(X_range, model.predict(poly.transform(X_range)), color="red")
plt.title("House Price Trend")
plt.xlabel("Size")
plt.ylabel("Price")
plt.show()


# Example 4: Predict Car Price using Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Car age in years
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)

# Price in Lakhs
y = np.array([10, 9, 7.5, 6, 5, 4.5])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Predict price for 7-year-old car
new_car = poly.transform([[7]])
print("Predicted Price:", model.predict(new_car)[0], "Lakhs")

# Plot
X_range = np.linspace(1,7,100).reshape(-1,1)

plt.scatter(X, y, color="blue")
plt.plot(X_range, model.predict(poly.transform(X_range)), color="red")
plt.title("Car Age vs Price")
plt.xlabel("Car Age")
plt.ylabel("Price")
plt.show()


# Example 5: Predict Sales using Advertisement Budget

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Ad budget in thousands
X = np.array([10, 20, 30, 40, 50, 60]).reshape(-1,1)

# Sales
y = np.array([100, 140, 210, 320, 470, 650])

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Predict sales for budget 45
new_data = poly.transform([[45]])
print("Predicted Sales:", model.predict(new_data)[0])

# Plot
X_range = np.linspace(10,60,100).reshape(-1,1)

plt.scatter(X, y, color="green")
plt.plot(X_range, model.predict(poly.transform(X_range)), color="red")
plt.title("Ad Budget vs Sales")
plt.xlabel("Budget")
plt.ylabel("Sales")
plt.show()


# Example 6: Compare Different Polynomial Degrees

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
y = np.array([5, 9, 15, 28, 50, 80])

plt.scatter(X, y, color="black")

for d in [1, 2, 3]:
    poly = PolynomialFeatures(degree=d)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    X_range = np.linspace(1,6,100).reshape(-1,1)
    y_pred = model.predict(poly.transform(X_range))

    plt.plot(X_range, y_pred, label=f"Degree {d}")

plt.title("Polynomial Degrees Comparison")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()




