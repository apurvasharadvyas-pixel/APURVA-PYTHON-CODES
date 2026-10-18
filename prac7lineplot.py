import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 70, 65, 80, 90]

plt.plot(days, marks, marker='o')
plt.title("Student Marks")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.grid(True)
plt.show()