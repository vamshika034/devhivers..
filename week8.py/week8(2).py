# Example 1: Predict House Prices using Size, Bedrooms, Bathrooms

import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Size': [1000, 1200, 1500, 1800, 2000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Bathrooms': [1, 2, 2, 3, 3],
    'Price': [50, 60, 75, 90, 100]   # in Lakhs
}

df = pd.DataFrame(data)

# Features and Target
X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Model
model = LinearRegression()
model.fit(X, y)

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:")
print("Size:", model.coef_[0])
print("Bedrooms:", model.coef_[1])
print("Bathrooms:", model.coef_[2])

# Prediction
new_house = [[1600, 3, 2]]
prediction = model.predict(new_house)

print("Predicted House Price:", prediction[0], "Lakhs")


# Example 2: Predict Exam Scores using Study Hours and Attendance

import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Study_Hours': [2, 4, 6, 8, 10],
    'Attendance': [60, 70, 75, 85, 95],
    'Score': [40, 50, 65, 80, 95]
}

df = pd.DataFrame(data)

# Features and Target
X = df[['Study_Hours', 'Attendance']]
y = df['Score']

# Model
model = LinearRegression()
model.fit(X, y)

# Coefficients
print("Intercept:", model.intercept_)
print("Study Hours Coefficient:", model.coef_[0])
print("Attendance Coefficient:", model.coef_[1])

# Prediction
new_student = [[7, 80]]
prediction = model.predict(new_student)

print("Predicted Exam Score:", prediction[0])

# Example 3: Check Multicollinearity using Correlation Matrix

import pandas as pd

data = {
    'Size': [1000, 1200, 1500, 1800, 2000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Bathrooms': [1, 2, 2, 3, 3]
}

df = pd.DataFrame(data)

# Correlation between predictors
print(df.corr())


# Example 4: Predict Car Price using Age, Mileage, Engine Size

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Age': [1, 2, 3, 4, 5],
    'Mileage': [10000, 20000, 30000, 40000, 50000],
    'Engine_Size': [1200, 1400, 1500, 1600, 1800],
    'Price': [9, 8, 7, 6, 5]   # in Lakhs
}

df = pd.DataFrame(data)

X = df[['Age', 'Mileage', 'Engine_Size']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict new car price
new_car = [[3, 25000, 1500]]
print("Predicted Price:", model.predict(new_car)[0], "Lakhs")


# Example 5: Predict Salary using Experience, Education Years

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Experience': [1, 2, 3, 4, 5],
    'Education_Years': [12, 14, 15, 16, 18],
    'Salary': [25000, 30000, 38000, 45000, 55000]
}

df = pd.DataFrame(data)

X = df[['Experience', 'Education_Years']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict salary
employee = [[4, 16]]
print("Predicted Salary:", model.predict(employee)[0])


# Example 6: Predict Sales using Advertising Budget and Discounts

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Ad_Budget': [10, 20, 30, 40, 50],
    'Discount': [5, 10, 15, 20, 25],
    'Sales': [100, 150, 220, 280, 350]
}

df = pd.DataFrame(data)

X = df[['Ad_Budget', 'Discount']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict sales
new_data = [[35, 18]]
print("Predicted Sales:", model.predict(new_data)[0])



