# Practice Project 1: Predict Employee Salary
# Compare Linear, Multiple, and Polynomial Regression

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

# Dataset
data = {
    'Experience': [1,2,3,4,5,6,7,8],
    'Age': [22,24,26,28,30,32,34,36],
    'Projects': [1,2,2,3,4,4,5,6],
    'Salary': [25000,30000,35000,42000,50000,58000,67000,76000]
}

df = pd.DataFrame(data)

# ---------------- Linear Regression ----------------
X1 = df[['Experience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.25, random_state=42)

linear = LinearRegression()
linear.fit(X_train, y_train)
pred1 = linear.predict(X_test)

print("Linear Regression")
print("R²:", r2_score(y_test, pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred1)))

# ---------------- Multiple Regression ----------------
X2 = df[['Experience', 'Age', 'Projects']]

X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.25, random_state=42)

multiple = LinearRegression()
multiple.fit(X_train, y_train)
pred2 = multiple.predict(X_test)

print("\nMultiple Regression")
print("R²:", r2_score(y_test, pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred2)))

# ---------------- Polynomial Regression ----------------
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X1)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=42)

poly_model = LinearRegression()
poly_model.fit(X_train, y_train)
pred3 = poly_model.predict(X_test)

print("\nPolynomial Regression")
print("R²:", r2_score(y_test, pred3))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred3)))



# Practice Project 2: Predict Product Sales
# Compare Linear, Multiple, and Polynomial Regression

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

# Dataset
data = {
    'Ad_Budget': [10,20,30,40,50,60,70,80],
    'Discount': [2,4,5,7,8,10,12,15],
    'Visitors': [100,150,220,300,380,460,550,650],
    'Sales': [50,70,95,130,170,220,280,350]
}

df = pd.DataFrame(data)

y = df['Sales']

# Linear Regression
X1 = df[['Ad_Budget']]
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.25, random_state=1)

model1 = LinearRegression()
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

print("Linear Regression")
print("R²:", r2_score(y_test, pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred1)))

# Multiple Regression
X2 = df[['Ad_Budget', 'Discount', 'Visitors']]
X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.25, random_state=1)

model2 = LinearRegression()
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

print("\nMultiple Regression")
print("R²:", r2_score(y_test, pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred2)))

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X1)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=1)

model3 = LinearRegression()
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

print("\nPolynomial Regression")
print("R²:", r2_score(y_test, pred3))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred3)))



# Practice Project 3: Predict Delivery Time

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

data = {
    'Distance': [2,4,6,8,10,12,14,16],
    'Traffic_Level': [1,1,2,2,3,3,4,4],
    'Orders': [1,1,2,2,3,3,4,5],
    'Time': [10,15,22,28,38,45,58,70]
}

df = pd.DataFrame(data)
y = df['Time']

# Linear
X1 = df[['Distance']]
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.25, random_state=2)

m1 = LinearRegression()
m1.fit(X_train, y_train)
p1 = m1.predict(X_test)

print("Linear Regression")
print("R²:", r2_score(y_test, p1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p1)))

# Multiple
X2 = df[['Distance', 'Traffic_Level', 'Orders']]
X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.25, random_state=2)

m2 = LinearRegression()
m2.fit(X_train, y_train)
p2 = m2.predict(X_test)

print("\nMultiple Regression")
print("R²:", r2_score(y_test, p2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p2)))

# Polynomial
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X1)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=2)

m3 = LinearRegression()
m3.fit(X_train, y_train)
p3 = m3.predict(X_test)

print("\nPolynomial Regression")
print("R²:", r2_score(y_test, p3))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p3)))



# Practice Project 4: Predict Gym Membership Revenue
# Compare Linear, Multiple, Polynomial Regression

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

data = {
    'Members': [50, 70, 90, 110, 130, 150, 170, 190],
    'Trainers': [2, 3, 3, 4, 4, 5, 5, 6],
    'Ads': [5, 7, 9, 12, 14, 16, 18, 20],
    'Revenue': [40, 55, 68, 85, 100, 120, 138, 160]
}

df = pd.DataFrame(data)
y = df['Revenue']

# Linear Regression
X1 = df[['Members']]
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.25, random_state=1)

model1 = LinearRegression()
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

print("Linear Regression")
print("R²:", r2_score(y_test, pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred1)))

# Multiple Regression
X2 = df[['Members', 'Trainers', 'Ads']]
X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.25, random_state=1)

model2 = LinearRegression()
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

print("\nMultiple Regression")
print("R²:", r2_score(y_test, pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred2)))

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X1)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=1)

model3 = LinearRegression()
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

print("\nPolynomial Regression")
print("R²:", r2_score(y_test, pred3))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred3)))


# Practice Project 5: Predict Restaurant Daily Orders

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

data = {
    'Customers': [30, 45, 60, 75, 90, 110, 130, 150],
    'Offers': [1, 2, 2, 3, 3, 4, 5, 6],
    'Rating': [3.5, 3.8, 4.0, 4.1, 4.3, 4.4, 4.6, 4.8],
    'Orders': [25, 38, 52, 66, 82, 100, 125, 150]
}

df = pd.DataFrame(data)
y = df['Orders']

# Linear
X1 = df[['Customers']]
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.25, random_state=2)

m1 = LinearRegression()
m1.fit(X_train, y_train)
p1 = m1.predict(X_test)

print("Linear Regression")
print("R²:", r2_score(y_test, p1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p1)))

# Multiple
X2 = df[['Customers', 'Offers', 'Rating']]
X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.25, random_state=2)

m2 = LinearRegression()
m2.fit(X_train, y_train)
p2 = m2.predict(X_test)

print("\nMultiple Regression")
print("R²:", r2_score(y_test, p2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p2)))

# Polynomial
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X1)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=2)

m3 = LinearRegression()
m3.fit(X_train, y_train)
p3 = m3.predict(X_test)

print("\nPolynomial Regression")
print("R²:", r2_score(y_test, p3))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p3)))



# Practice Project 6: Predict Crop Yield

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

data = {
    'Rainfall': [20, 30, 40, 50, 60, 70, 80, 90],
    'Fertilizer': [5, 8, 10, 12, 15, 18, 20, 22],
    'Temperature': [25, 26, 27, 28, 29, 30, 31, 32],
    'Yield': [10, 18, 28, 40, 55, 68, 78, 85]
}

df = pd.DataFrame(data)
y = df['Yield']

# Linear
X1 = df[['Rainfall']]
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.25, random_state=3)

m1 = LinearRegression()
m1.fit(X_train, y_train)
p1 = m1.predict(X_test)

print("Linear Regression")
print("R²:", r2_score(y_test, p1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p1)))

# Multiple
X2 = df[['Rainfall', 'Fertilizer', 'Temperature']]
X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.25, random_state=3)

m2 = LinearRegression()
m2.fit(X_train, y_train)
p2 = m2.predict(X_test)

print("\nMultiple Regression")
print("R²:", r2_score(y_test, p2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p2)))

# Polynomial
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X1)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=3)

m3 = LinearRegression()
m3.fit(X_train, y_train)
p3 = m3.predict(X_test)

print("\nPolynomial Regression")
print("R²:", r2_score(y_test, p3))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p3)))



