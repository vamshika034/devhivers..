import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# Normal Distribution
x = np.linspace(0, 100, 200)
y = norm.pdf(x, 50, 10)

plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.title("Normal Distribution")
plt.xlabel("Exam Scores")
plt.ylabel("Probability Density")
plt.show()

# Binomial Distribution
n = 10
p = 0.5
x = np.arange(0, 11)
y = binom.pmf(x, n, p)

plt.figure(figsize=(6,4))
plt.bar(x, y)
plt.title("Binomial Distribution")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.show()

# Poisson Distribution
lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)

plt.figure(figsize=(6,4))
plt.bar(x, y)
plt.title("Poisson Distribution")
plt.xlabel("Calls per Hour")
plt.ylabel("Probability")
plt.show()