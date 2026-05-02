#Train Random Forest Classifier
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
digits = load_digits()
X = digits.data
y = digits.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

# Accuracy
rf_acc = rf.score(X_test, y_test)
print("Random Forest Accuracy:", rf_acc)

#Train Single Decision Tree (Comparison)
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

dt_acc = dt.score(X_test, y_test)
print("Decision Tree Accuracy:", dt_acc)

#Feature Importance Analysis
import matplotlib.pyplot as plt

importances = rf.feature_importances_

# Plot top 10 important features
indices = importances.argsort()[-10:]

plt.barh(range(len(indices)), importances[indices])
plt.yticks(range(len(indices)), indices)
plt.xlabel("Importance")
plt.title("Top Pixel Importance")
plt.show()

#Predict a Digit
sample = X_test[0].reshape(1, -1)
prediction = rf.predict(sample)

print("Predicted Digit:", prediction[0])
