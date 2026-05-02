#Build Decision Tree Classifier
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Accuracy
print("Accuracy:", model.score(X_test, y_test))

#Visualize the Tree Structure
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(12,8))
plot_tree(model, feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True)
plt.show()

#Experiment with Tree Depth
# Shallow tree
model1 = DecisionTreeClassifier(max_depth=2)
model1.fit(X_train, y_train)

# Deeper tree
model2 = DecisionTreeClassifier(max_depth=5)
model2.fit(X_train, y_train)

print("Depth 2 Accuracy:", model1.score(X_test, y_test))
print("Depth 5 Accuracy:", model2.score(X_test, y_test))

#Try Different Splitting Criteria
# Gini (default)
gini_model = DecisionTreeClassifier(criterion='gini')

# Entropy
entropy_model = DecisionTreeClassifier(criterion='entropy')

gini_model.fit(X_train, y_train)
entropy_model.fit(X_train, y_train)

print("Gini Accuracy:", gini_model.score(X_test, y_test))
print("Entropy Accuracy:", entropy_model.score(X_test, y_test))

#Predict New Flower
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("Predicted Class:", iris.target_names[prediction][0])