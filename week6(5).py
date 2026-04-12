import numpy as np
from scipy.stats import ttest_ind, chisquare

# -------------------
# t-test example
# -------------------
class_A = [70, 75, 80, 85, 90]
class_B = [60, 65, 70, 75, 80]

t_stat, p_value = ttest_ind(class_A, class_B)

print("T-Test")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("Not significant")

# -------------------
# Chi-square example
# -------------------
observed = [30, 20]
expected = [25, 25]

chi_stat, p_value = chisquare(observed, expected)

print("\nChi-Square Test")
print("chi-square statistic:", chi_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("Not significant")