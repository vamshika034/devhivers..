#Train a Spam Classifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.linear_model import LogisticRegression

# Example dataset (simple)
X = [[1], [2], [3], [4], [5], [6]]   # e.g., spam score
y = [0, 0, 0, 1, 1, 1]              # 0 = not spam, 1 = spam

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

#Generate Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#Calculate Precision and Recall
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Precision:", precision)
print("Recall:", recall)

