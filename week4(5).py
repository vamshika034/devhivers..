# Label Encoding
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {'Gender': ['Male', 'Female', 'Female', 'Male']}
df = pd.DataFrame(data)

encoder = LabelEncoder()
df['Gender_encoded'] = encoder.fit_transform(df['Gender'])

print(df)

#One-Hot Encoding
import pandas as pd

data = {'Department': ['HR', 'IT', 'Sales', 'IT']}
df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['Department'])
print(df_encoded)

#One-Hot Encoding Using Scikit-learn
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[['Department']]).toarray()
print(encoded)

#Encoding Ordinal Variables
data = {'Level': ['Low', 'Medium', 'High']}
df = pd.DataFrame(data)

mapping = {'Low': 1, 'Medium': 2, 'High': 3}
df['Level_encoded'] = df['Level'].map(mapping)

print(df)

#Example: Encode Multiple Columns
data = {
    'Gender': ['Male', 'Female', 'Female'],
    'Department': ['HR', 'IT', 'Sales']
}

df = pd.DataFrame(data)

df = pd.get_dummies(df, columns=['Department'])

#Real Example: Student Dataset
data = {
    'Gender': ['Male', 'Female', 'Male'],
    'Branch': ['CSE', 'ECE', 'CSE']
}

df = pd.DataFrame(data)

# Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# One-hot encoding
df = pd.get_dummies(df, columns=['Branch'])

print(df)
