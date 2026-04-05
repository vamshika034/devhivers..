#Histogram using sns.histplot()
import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 50]

sns.histplot(data)

plt.title("Basic Histogram")
plt.show()

#KDE Plot using sns.kdeplot()
import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 50]

sns.kdeplot(data)

plt.title("KDE Distribution")
plt.show()

#Histogram + KDE Together
import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 50]

sns.histplot(data, kde=True)

plt.title("Histogram with KDE")
plt.show()

#Using Seaborn Built-in Dataset
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(tips['total_bill'])

plt.title("Total Bill Distribution")
plt.show()

#Compare Distributions Across Gender
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(data=tips, x="total_bill", hue="sex", kde=True)

plt.title("Bill Distribution by Gender")
plt.show()

#Customize Colors & Style
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")

tips = sns.load_dataset("tips")

sns.histplot(tips['total_bill'], color="purple", kde=True)
plt.title("Styled Distribution")
plt.show()