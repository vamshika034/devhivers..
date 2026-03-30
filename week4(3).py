#Detect Outliers Using IQR Method
import pandas as pd

data = {'Marks': [60, 65, 70, 75, 80, 150]}
df = pd.DataFrame(data)

Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Marks'] < lower) | (df['Marks'] > upper)]
print(outliers)

#Detect Outliers Using Z-Score
from scipy import stats

df['zscore'] = stats.zscore(df['Marks'])
outliers = df[df['zscore'] > 3]
print(outliers)

#Visualize Outliers with Boxplot
import matplotlib.pyplot as plt

plt.boxplot(df['Marks'])
plt.show()

#Visualize Using Scatter Plot
plt.scatter(range(len(df)), df['Marks'])
plt.show()

#Remove Outliers
df_clean = df[(df['Marks'] >= lower) & (df['Marks'] <= upper)]

#Cap Outliers (Replace Extreme Values)
df['Marks'] = df['Marks'].clip(lower, upper)

#Transform Outliers (Log Transformation)
import numpy as np
df['Marks'] = np.log(df['Marks'])

#Example: Extreme Sales Values
data = {'Sales': [100, 120, 130, 140, 5000]}
df = pd.DataFrame(data)

plt.boxplot(df['Sales'])
plt.show()