import numpy as np
import matplotlib.pyplot as plt

# Create population data (heights)
population = np.random.randint(150, 190, 1000)

# Draw multiple random samples
sample_means = []

for i in range(100):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

# Plot histogram of sample means
plt.figure(figsize=(6,4))
plt.hist(sample_means, bins=15)
plt.title("Central Limit Theorem - Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

print("Average of sample means:", np.mean(sample_means))