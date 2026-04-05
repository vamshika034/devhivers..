#Create Sample Dataset (Customer Data)
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50],
    "Income": [20000, 25000, 30000, 35000, 40000, 45000, 50000],
    "Spending": [1500, 1800, 2000, 2200, 2400, 2600, 2800],
    "Savings": [5000, 6000, 7000, 8000, 9000, 10000, 11000]
}

df = pd.DataFrame(data)
print(df)

#Scatter Plot (Age vs Income)
sns.scatterplot(x="Age", y="Income", data=df)

plt.title("Age vs Income")
plt.show()

#Scatter Plot (Income vs Spending)
sns.scatterplot(x="Income", y="Spending", data=df)

plt.title("Income vs Spending")
plt.show()

#Box Plot (Detect Outliers)
sns.boxplot(data=df)

plt.title("Box Plot of Customer Data")
plt.show()

#Correlation Heatmap
corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

#Pair Plot (All Relationships Together)
sns.pairplot(df)

plt.show()

#Combined Styled Visualization
sns.set_style("whitegrid")

plt.figure(figsize=(8,5))

sns.scatterplot(x="Age", y="Spending", data=df, color="purple")

plt.title("Age vs Spending Pattern")
plt.tight_layout()

plt.show()