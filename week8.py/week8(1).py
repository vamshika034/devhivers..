# Linear Regression Example
# Predict Student Scores Based on Study Hours

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Independent Variable (Study Hours)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Dependent Variable (Scores)
y = np.array([35, 40, 50, 55, 65, 70])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Get slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

print("Slope (Coefficient):", slope)
print("Intercept:", intercept)

# Predict score for 7 study hours
new_hours = np.array([[7]])
predicted_score = model.predict(new_hours)

print("Predicted Score for 7 Hours:", predicted_score[0])

# Plot data points
plt.scatter(X, y, color="blue", label="Actual Data")

# Plot regression line
plt.plot(X, model.predict(X), color="red", label="Regression Line")

# Labels
plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.legend()
plt.show()


# Example 1: Predict House Price Based on Size

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# House size in square feet
X = np.array([500, 800, 1000, 1200, 1500, 1800]).reshape(-1, 1)

# House prices in lakhs
y = np.array([20, 30, 40, 45, 55, 65])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict price for 1400 sq ft
print("Predicted Price:", model.predict([[1400]])[0], "Lakhs")

plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.title("House Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price (Lakhs)")
plt.show()


# Example 2: Predict Salary Based on Experience

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Experience in years
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Salary in thousands
y = np.array([25, 30, 35, 40, 45, 50])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict salary for 7 years experience
print("Predicted Salary:", model.predict([[7]])[0], "Thousands")

plt.scatter(X, y, color="green")
plt.plot(X, model.predict(X), color="red")
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()



# Example 3: Predict Ice Cream Sales Based on Temperature

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Temperature in Celsius
X = np.array([20, 22, 25, 28, 30, 35]).reshape(-1, 1)

# Sales
y = np.array([100, 120, 150, 170, 200, 250])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict sales at 32°C
print("Predicted Sales:", model.predict([[32]])[0])

plt.scatter(X, y, color="orange")
plt.plot(X, model.predict(X), color="red")
plt.title("Temperature vs Ice Cream Sales")
plt.xlabel("Temperature (°C)")
plt.ylabel("Sales")
plt.show()


# Example 4: Predict Car Price Based on Age

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Car age in years
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Price in lakhs
y = np.array([8, 7.5, 7, 6, 5.5, 5])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict price for 7-year-old car
print("Predicted Price:", model.predict([[7]])[0], "Lakhs")

plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.title("Car Age vs Price")
plt.xlabel("Age (Years)")
plt.ylabel("Price")
plt.show()


# Example 5: Predict Electricity Bill Based on Units Used

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Units consumed
X = np.array([50, 100, 150, 200, 250, 300]).reshape(-1, 1)

# Bill amount
y = np.array([200, 400, 600, 800, 1000, 1200])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict bill for 180 units
print("Predicted Bill:", model.predict([[180]])[0])

plt.scatter(X, y, color="green")
plt.plot(X, model.predict(X), color="red")
plt.title("Units Used vs Electricity Bill")
plt.xlabel("Units")
plt.ylabel("Bill Amount")
plt.show()


# Example 6: Predict Mobile Battery Life Based on Usage Hours

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Usage hours
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Battery remaining %
y = np.array([95, 85, 75, 65, 55, 45])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict battery after 7 hours
print("Predicted Battery:", model.predict([[7]])[0], "%")

plt.scatter(X, y, color="orange")
plt.plot(X, model.predict(X), color="red")
plt.title("Usage Hours vs Battery Life")
plt.xlabel("Usage Hours")
plt.ylabel("Battery %")
plt.show()


