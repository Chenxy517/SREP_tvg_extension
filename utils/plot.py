import matplotlib.pyplot as plt

# Data
x1 = list(range(2, 16))
x1.append(20)
x1.append(25)
x1.append(30)
y1_col2 = [21.031, 32.287, 43.11, 55.932, 64.945, 71.764, 79.406, 87.002, 93.377]
y1_col3 = [20, 60, 102, 150, 191, 266, 308, 388, 432]
sim2 = [19, 59.459, 85.297, 112.89, 134.784, 155.164, 179.423, 199.352, 215.771, 230.427, 247.344, 262.955, 281.677, 298.82, 377.59, 455.186, 535.057]
ana2 = [20, 55.141, 78.566, 101.759, 124.633, 147.332, 169.451, 191.287, 213.419, 235.252, 257.165, 278.828, 300.151, 321.699, 430.21 , 534.923, 640.353]


x2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40]
y2_col2 = [21.031, 32.287, 43.11, 55.932, 64.945, 71.764, 79.406, 87.002, 93.377, 155.74, 211.133, 265.97]

# Figure 1
plt.figure(figsize=(10, 6))
plt.plot(x1, sim2, marker='o', label='Simulation')
plt.plot(x1, ana2, marker='o', label='Analysis')
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
plt.title('Performance(model1)')
plt.legend()
plt.grid(True)
plt.show()

# Figure 3
plt.figure(figsize=(10, 6))
plt.plot(x1, sim2, marker='o', label='Simulation')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Performance(model2)')
plt.legend()
plt.grid(True)
plt.show()

# Figure 4
plt.figure(figsize=(10, 6))
plt.plot(x2, y2_col2, marker='o', label='Model1')
plt.plot(x1, sim2, marker='o', label='Model2')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparison')
plt.legend()
plt.grid(True)
plt.show()