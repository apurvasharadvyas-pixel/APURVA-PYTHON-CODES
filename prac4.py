
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate random numbers between 0 and 1
rand_data = np.random.rand(10)
print("1. Random numbers (rand):", rand_data)

# 2. Generate standard normal random numbers
randn_data = np.random.randn(10)
print("\n2. Standard normal (randn):", randn_data)

# 3. Generate random integers from 1 to 9
randint_data = np.random.randint(1, 10, size=10)
print("\n3. Random integers (randint):", randint_data)

# 4. Generate normal distribution (mean=50, std=10)
normal_data = np.random.normal(loc=50, scale=10, size=10000)
print("\n4. Normal distribution (first 10):", normal_data[:10])

# 5. Generate uniform random numbers using random()
random_data = np.random.random(10)
print("\n5. Random values (random):", random_data)

# 6. Simulate 1000 rolls of a six-sided die
dice = np.random.randint(1, 7, size=1000)
print("\n6. First 10 dice rolls:", dice[:10])

# 7. Compute statistics for the normal distribution
print("\n7. STATISTICS OF NORMAL DISTRIBUTION")
print("Sample size:", len(normal_data))
print("Mean:", np.mean(normal_data))
print("Median:", np.median(normal_data))
print("Variance:", np.var(normal_data))
print("Standard deviation:", np.std(normal_data))
print("Minimum:", np.min(normal_data))
print("Maximum:", np.max(normal_data))
print("25th percentile:", np.percentile(normal_data, 25))
print("75th percentile:", np.percentile(normal_data, 75))

# 8. Compute statistics for dice rolls
print("\n8. STATISTICS OF DICE ROLLS")
print("Mean:", np.mean(dice))
print("Median:", np.median(dice))
print("Variance:", np.var(dice))
print("Standard deviation:", np.std(dice))

# 9. Count each dice face
print("\n9. DICE FACE FREQUENCIES")
for face in range(1, 7):
    print(f"Face {face}: {np.sum(dice == face)} times")

# 10. Demonstrate modern NumPy random generator
rng = np.random.default_rng(42)
modern_data = rng.normal(50, 10, 1000)

print("\n10. MODERN NUMPY GENERATOR")
print("Mean:", np.mean(modern_data))
print("Standard deviation:", np.std(modern_data))
