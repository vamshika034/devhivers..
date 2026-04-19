#Predict Student Scores Dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dataset
X = np.array([[1],[2],[3],[4],[5],[6],[7]])
y = np.array([30,40,50,60,70,80,90])

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Predictions:", y_pred)
print("Actual:", y_test)
print("RMSE:", rmse)



#Plot Regression Line
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.legend()
plt.show()


#Remove Missing Values
import pandas as pd

df = pd.DataFrame({
    "Hours":[1,2,None,4,5],
    "Score":[30,40,50,60,70]
})

df = df.dropna()
print(df)

#Convert Column Shapes
X = df[["Hours"]]
y = df["Score"]




#80/20 Split
train_test_split(X, y, test_size=0.2, random_state=1)

#70/30 Split
train_test_split(X, y, test_size=0.3, random_state=1)



#Train Regression Model Examples
Example 1
model = LinearRegression()
model.fit(X_train, y_train)

#Example 2 (Print Coefficients)
print(model.coef_)
print(model.intercept_)

#Evaluate with RMSE Examples
Example 1
from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(rmse)


#Compare Actual vs Predicted
for actual, pred in zip(y_test, y_pred):
    print("Actual:", actual, "Predicted:", round(pred,2))



