import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set up figure size and layout
plt.figure(figsize=(16, 20))

# 1. Normal Distribution
plt.subplot(5, 2, 1)
data = np.random.normal(loc=0, scale=1, size=1000)
sns.histplot(data, kde=True)
plt.title("Normal Distribution")

# 2. Binomial Distribution
plt.subplot(5, 2, 2)
data = np.random.binomial(n=10, p=0.5, size=1000)
sns.histplot(data, kde=False)
plt.title("Binomial Distribution")

# 3. Poisson Distribution
plt.subplot(5, 2, 3)
data = np.random.poisson(lam=5, size=1000)
sns.histplot(data, kde=False)
plt.title("Poisson Distribution")

# 4. Uniform Distribution
plt.subplot(5, 2, 4)
data = np.random.uniform(low=0, high=10, size=1000)
sns.histplot(data, kde=True)
plt.title("Uniform Distribution")

# 5. Exponential Distribution
plt.subplot(5, 2, 5)
data = np.random.exponential(scale=1, size=1000)
sns.histplot(data, kde=True)
plt.title("Exponential Distribution")

# 6. Beta Distribution
plt.subplot(5, 2, 6)
data = np.random.beta(a=2, b=5, size=1000)
sns.histplot(data, kde=True)
plt.title("Beta Distribution")

# 7. Gamma Distribution
plt.subplot(5, 2, 7)
data = np.random.gamma(shape=2, scale=2, size=1000)
sns.histplot(data, kde=True)
plt.title("Gamma Distribution")

# 8. Chi-Square Distribution
plt.subplot(5, 2, 8)
data = np.random.chisquare(df=3, size=1000)
sns.histplot(data, kde=True)
plt.title("Chi-Square Distribution")

# 9. Log-Normal Distribution
plt.subplot(5, 2, 9)
data = np.random.lognormal(mean=0, sigma=1, size=1000)
sns.histplot(data, kde=True)
plt.title("Log-Normal Distribution")

# 10. Geometric Distribution
plt.subplot(5, 2, 10)
data = np.random.geometric(p=0.3, size=1000)
sns.histplot(data, kde=False)
plt.title("Geometric Distribution")

# Adjust layout
plt.tight_layout()
plt.show()
