"""
3d Path visualization
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from shortest_path_on_surface import shortest_path


matrix = np.array([[random.randint(0, 5) for _ in range(5)] for _ in range(5)])
path = np.array(shortest_path(matrix, 1, (0, 0), (4, 4)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y = np.meshgrid(np.arange(matrix.shape[1]), np.arange(matrix.shape[0]))

ax.plot_surface(x, y, matrix+0.1, cmap='viridis', alpha=0.5)

ax.plot(path[:, 1], path[:, 0], matrix[path[:, 0], path[:, 1]],
    color='red', marker='o', markersize=8, linestyle='-', linewidth=2)

ax.set_xlabel('Column Index')
ax.set_ylabel('Row Index')
ax.set_zlabel('Height')

ax.set_title('3D path visualisation')
plt.show()
