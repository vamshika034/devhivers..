#Supervised Learning – #Classification Example
#Predict Pass / Fail from Marks

from sklearn.tree import DecisionTreeClassifier

# Input marks
X = [[30], [40], [50], [60], [70], [80]]

# Output: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for new student
print(model.predict([[55]]))

#Supervised Learning – Regression Example
#Predict Salary from Experience

from sklearn.linear_model import LinearRegression

# Experience in years
X = [[1], [2], [3], [4], [5]]

# Salary
y = [20000, 30000, 40000, 50000, 60000]

model = LinearRegression()
model.fit(X, y)

# Predict salary for 6 years experience
print(model.predict([[6]]))


#Unsupervised Learning – Clustering Example
#Group Customers by Spending

from sklearn.cluster import KMeans

X = [[10], [15], [20], [80], [85], [90]]

model = KMeans(n_clusters=2)
model.fit(X)

print(model.labels_)


#Unsupervised Learning – Student Groups
#Group Students by Study Hours

from sklearn.cluster import KMeans

X = [[1], [2], [3], [8], [9], [10]]

model = KMeans(n_clusters=2)
model.fit(X)

print(model.labels_)


#Supervised Learning – Email Spam Detection

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

texts = ["win money now", "free prize", "hello friend", "how are you"]
labels = [1, 1, 0, 0]   # 1=Spam, 0=Normal

cv = CountVectorizer()
X = cv.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

test = cv.transform(["free money"])
print(model.predict(test))


#Unsupervised Learning – Dimensionality Reduction
#Reduce 3 Features to 2 Features


from sklearn.decomposition import PCA
import numpy as np

X = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

pca = PCA(n_components=2)
result = pca.fit_transform(X)

print(result)

