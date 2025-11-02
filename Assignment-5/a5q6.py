import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 1, 8]

plt.plot(x, y, marker='o')
plt.title("Plot of x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()