import matplotlib.pyplot as plt

# Data
x1 = list(range(2, 11))
y1_col2 = [21.031, 32.287, 43.11, 55.932, 64.945, 71.764, 79.406, 87.002, 93.377]
y1_col3 = [20, 60, 102, 150, 191, 266, 308, 388, 432]

x2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40]
y2_col2 = [21.031, 32.287, 43.11, 55.932, 64.945, 71.764, 79.406, 87.002, 93.377, 155.74, 211.133, 265.97]

# Figure 1
plt.figure(figsize=(10, 6))
plt.plot(x1, y1_col2, marker='o', label='Simulation')
plt.plot(x1, y1_col3, marker='o', label='Analysis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparison')
plt.legend()
plt.grid(True)
plt.show()

# Figure 2
plt.figure(figsize=(10, 6))
plt.plot(x2, y2_col2, marker='o', label='Simulation')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Performance(2-40)')
plt.legend()
plt.grid(True)
plt.show()
