#Basic Box Plot
import seaborn as sns
import matplotlib.pyplot as plt

marks = [40, 45, 50, 55, 60, 65, 70, 90]

sns.boxplot(data=marks)

plt.title("Box Plot of Marks")
plt.show()

#Box Plot by Category
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "subject": ["Math", "Math", "Science", "Science"],
    "marks": [60, 80, 70, 90]
}

import pandas as pd
df = pd.DataFrame(data)

sns.boxplot(x="subject", y="marks", data=df)

plt.title("Marks by Subject")
plt.show()
#Box Plot using Built-in Dataset
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", data=tips)

plt.title("Total Bill by Day")
plt.show()

#Heatmap (Correlation Matrix)
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

sns.heatmap(corr)

plt.title("Correlation Heatmap")
plt.show()

#Customized Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Styled Heatmap")
plt.show()
