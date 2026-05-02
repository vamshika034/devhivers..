#Python Implementation
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Dataset
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Predictions
x_test = np.linspace(0, 7, 100).reshape(-1, 1)
y_prob = model.predict_proba(x_test)[:, 1]

# Plot
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(x_test, y_prob, color='blue', label='Logistic Curve')
plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()

#Interpreting Predicted Probabilities
# Predict probability for a new student
hours = [[3.5]]
prob = model.predict_proba(hours)[0][1]

print("Probability of Passing:", prob)

#Email Spam Detection
import numpy as np
from sklearn.linear_model import LogisticRegression

# Features: [links, length, spam_words]
X = np.array([
    [5, 100, 10],
    [1, 500, 1],
    [3, 200, 5],
    [0, 600, 0]
])

y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# Predict new email
email = [[2, 300, 4]]
print("Spam Probability:", model.predict_proba(email)[0][1])

#Customer Purchase Prediction
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([
    [22, 20000],
    [25, 25000],
    [47, 50000],
    [52, 60000]
])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Predict
customer = [[30, 30000]]
print("Purchase Probability:", model.predict_proba(customer)[0][1])