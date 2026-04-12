import numpy as np

scores = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

mean = np.mean(scores)
median = np.median(scores)
variance = np.var(scores)
std_dev = np.std(scores)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)