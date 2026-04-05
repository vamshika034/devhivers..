#Histogram (Exam Scores)
import matplotlib.pyplot as plt

scores = [45, 50, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.hist(scores)

plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Exam Score Distribution")

plt.show()

#Histogram with Bin Size
import matplotlib.pyplot as plt

scores = [45, 50, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.hist(scores, bins=5)

plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Histogram with 5 Bins")

plt.show()

#Scatter Plot (Height vs Weight)
import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170, 175, 180]
weight = [50, 55, 60, 65, 70, 75, 80]

plt.scatter(height, weight)

plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight")

plt.show()

#Scatter Plot with Colors
import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170, 175, 180]
weight = [50, 55, 60, 65, 70, 75, 80]

plt.scatter(height, weight, color='red')

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Colored Scatter Plot")

plt.show()

#Scatter Plot with Size Variation
import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170]
weight = [50, 55, 60, 65, 70]
sizes = [50, 100, 150, 200, 250]

plt.scatter(height, weight, s=sizes)

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter Plot with Sizes")

plt.show()