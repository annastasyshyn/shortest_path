"""
The program visualizes the algorithm for finding the shortest\
path between two surface points in 2D format
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from shortest_path_on_surface import shortest_path
matrix = np.array([[random.randint(0, 5) for _ in range(5)] for _ in range(5)])
path = np.array(shortest_path(matrix, 1, (0, 0), (4, 4)))

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap='magma')

ax.plot(path[:, 1], path[:, 0], color='yellow', marker='o',
markersize=10, linestyle='-', linewidth=2)

cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Height')
ax.set_xlabel('Column Index')
ax.set_ylabel('Row Index')
ax.set_title('2D path visualisation')

plt.show()
