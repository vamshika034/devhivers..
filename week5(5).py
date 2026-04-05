#Sample Data
import matplotlib.pyplot as plt
import seaborn as sns

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 250, 300, 280, 350]

#Apply Seaborn Theme
sns.set_style("darkgrid")

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.show()

#Customize Colors & Fonts
sns.set_style("whitegrid")

plt.plot(months, sales, color="purple", linewidth=3)

plt.title("Monthly Sales", fontsize=16, fontweight="bold")
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales", fontsize=12)

plt.show()

#Adjust Figure Size
plt.figure(figsize=(8,5))

plt.plot(months, sales, color="green")

plt.title("Sales Trend")
plt.show()

#Add Gridlines
plt.plot(months, sales)

plt.grid(True)

plt.title("Sales with Grid")
plt.show()

#Add Annotation (Highlight Point)
plt.plot(months, sales, marker="o")

plt.annotate("Highest Sales",
             xy=("May", 350),
             xytext=("Mar", 330),
             arrowprops=dict(facecolor='black'))

plt.title("Sales Trend with Annotation")
plt.show()

#Improve Layout
plt.figure(figsize=(8,5))

plt.plot(months, sales, color="blue", marker="o")

plt.title("Styled Sales Plot")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()

#Full Styled Example (All Together)
import matplotlib.pyplot as plt
import seaborn as sns

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 250, 300, 280, 350]

sns.set_style("whitegrid")

plt.figure(figsize=(9,5))

plt.plot(months, sales, color="purple", linewidth=3, marker="o")

plt.title("Monthly Sales Trend", fontsize=16, fontweight="bold")
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales", fontsize=12)

plt.annotate("Peak",
             xy=("May", 350),
             xytext=("Mar", 330),
             arrowprops=dict(facecolor='black'))

plt.tight_layout()

plt.show()
