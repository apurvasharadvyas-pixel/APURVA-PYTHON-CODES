import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print("Addition:", a + b)
print("Multiplication:", a * b)
print("np.add:", (a, b))
print("np.sqrt:", np.sqrt(a))
print("np.exp:", np.exp(a))
c = np.array([10, 20, 30])
d = 5
print("Broadcasting:", c + d)
x = np.array([[1, 2, 3],[4, 5, 6]])
y = np.array([10, 20, 30])
print("2D Broadcasting:", x + y)