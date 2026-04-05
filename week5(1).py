#Line Plot (Monthly Sales Trend)
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 200, 180, 250]

plt.plot(months, sales)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")

plt.show()

#Bar Chart (Product Comparison)

#Multiple Line Plot + Legend
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
product_A = [100, 120, 140, 160]
product_B = [90, 110, 130, 150]

plt.plot(months, product_A, label="Product A")
plt.plot(months, product_B, label="Product B")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison")

plt.legend()

plt.show()

#Multiple Bars + Legend
import matplotlib.pyplot as plt
import numpy as np

products = ['A', 'B', 'C']
sales_2023 = [100, 120, 140]
sales_2024 = [110, 130, 150]

x = np.arange(len(products))

plt.bar(x - 0.2, sales_2023, width=0.4, label="2023")
plt.bar(x + 0.2, sales_2024, width=0.4, label="2024")

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Yearly Comparison")

plt.xticks(x, products)
plt.legend()

plt.show()

