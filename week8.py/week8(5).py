# Case Study: House Price Prediction using Multiple Regression

# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Step 2: Create Dataset
data = {
    'Size': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2700],
    'Bedrooms': [2, 3, 3, 4, 4, 5, 5, 6],
    'Bathrooms': [1, 2, 2, 3, 3, 4, 4, 5],
    'Price': [50, 60, 75, 90, 100, 115, 130, 145]
}

df = pd.DataFrame(data)

# Step 3: Features and Target
X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 5: Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluation
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("R² Score:", r2)
print("RMSE:", rmse)

# Step 8: Compare Actual vs Predicted
result = pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': y_pred
})

print("\nActual vs Predicted Prices")
print(result)

# Step 9: Predict New House Price
new_house = [[1600, 3, 2]]
prediction = model.predict(new_house)

print("\nPredicted Price for New House:", prediction[0], "Lakhs")


# Example 2: House Price Prediction with Garage and Location Score

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Dataset
data = {
    'Size': [1200, 1500, 1800, 2000, 2300, 2600],
    'Bedrooms': [2, 3, 3, 4, 4, 5],
    'Garage': [1, 1, 2, 2, 2, 3],
    'Location_Score': [6, 7, 8, 8, 9, 10],
    'Price': [55, 72, 88, 102, 120, 145]
}

df = pd.DataFrame(data)

X = df[['Size', 'Bedrooms', 'Garage', 'Location_Score']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

print(pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred
}))


# Example 3: House Price Prediction using CSV File

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load CSV file
# Replace filename with your file
df = pd.read_csv("house_data.csv")

# Assume columns: Size, Bedrooms, Bathrooms, Price
X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

print(pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': y_pred
}))

# Example 4: Predict New House Prices after Training

import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Size': [1000, 1400, 1600, 2000, 2400],
    'Bedrooms': [2, 3, 3, 4, 5],
    'Bathrooms': [1, 2, 2, 3, 4],
    'Price': [48, 68, 78, 105, 135]
}

df = pd.DataFrame(data)

X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

# New houses
new_houses = [
    [1500, 3, 2],
    [2200, 4, 3],
    [2600, 5, 4]
]

predictions = model.predict(new_houses)

print("Predicted House Prices:")
for i in range(len(new_houses)):
    print(new_houses[i], "->", predictions[i], "Lakhs")

    

