# Example 1: R² and RMSE for Linear Regression (Exam Scores)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
y = np.array([35, 40, 50, 55, 65, 70])

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Metrics
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print("R² Score:", r2)
print("RMSE:", rmse)


# Example 2: R² and RMSE for Multiple Regression (House Prices)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Dataset
data = {
    'Size': [1000, 1200, 1500, 1800, 2000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Bathrooms': [1, 2, 2, 3, 3],
    'Price': [50, 60, 75, 90, 100]
}

df = pd.DataFrame(data)

X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Metrics
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print("R² Score:", r2)
print("RMSE:", rmse)


# Example 3: Compare Linear vs Polynomial Regression

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

# Data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
y = np.array([10, 18, 28, 45, 65, 90])

# Linear Regression
linear = LinearRegression()
linear.fit(X, y)
y_pred_linear = linear.predict(X)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)

# Metrics
print("Linear Regression")
print("R²:", r2_score(y, y_pred_linear))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred_linear)))

print("\nPolynomial Regression")
print("R²:", r2_score(y, y_pred_poly))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred_poly)))


# Example 4: Student Score Prediction Evaluation

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Study hours vs score
X = np.array([2, 3, 4, 5, 6, 7]).reshape(-1,1)
y = np.array([40, 50, 55, 65, 70, 80])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("R² Score:", r2_score(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))


# Example 5: Car Price Prediction Evaluation

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Car age vs price
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
y = np.array([10, 9, 8, 7, 6, 5])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("R² Score:", r2_score(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))


# Example 6: House Price - Polynomial Regression Evaluation

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# House size vs price
X = np.array([500, 700, 900, 1100, 1300, 1500]).reshape(-1,1)
y = np.array([20, 28, 40, 58, 80, 110])

# Polynomial Features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

print("R² Score:", r2_score(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))

