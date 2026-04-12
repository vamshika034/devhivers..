import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Dataset
scores = np.array([65, 70, 72, 75, 78, 80, 82, 85, 88, 90])

# Mean
mean = np.mean(scores)

# Median
median = np.median(scores)

# Variance
variance = np.var(scores)

# Standard deviation
std_dev = np.std(scores)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

# Probability
prob_above_80 = np.sum(scores > 80) / len(scores)
print("Probability of marks above 80:", prob_above_80)

# Histogram
plt.figure(figsize=(6,4))
plt.hist(scores, bins=5)
plt.title("Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# T-test
class_A = [65, 70, 75, 80, 85]
class_B = [60, 65, 70, 75, 80]

t_stat, p_value = ttest_ind(class_A, class_B)

print("T-test p-value:", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("Not significant")