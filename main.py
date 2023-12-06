"""Finding the shortest path between two points on the on the surface"""
import heapq
import numpy as np
import pandas as pd
from numba import jit, int64, float64


def read_matrix_from_csv(file_path):
    """
    Read matrix from csv
    """
    return pd.read_csv(file_path, header=None).to_numpy()

@jit(nopython=True)
def calculate_distance(height_diff, step):
    """
    Calculate the physical distance between two points.
    (The square root of the sum of the squares of the 
    height difference and the number step)
    """
    return np.sqrt(height_diff**2 + step**2)

@jit(nopython=True)
def heuristic(node, end, step):
    """
    Heuristic function
    """
    return np.sqrt((node[0] - end[0])**2 + (node[1] - end[1])**2) * step

@jit(nopython=True)
def get_neighbors(x, y, rows, cols):
    """
    Get neighbours of a node
    """
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append((nx, ny))
    return neighbors

@jit(nopython=True)
def shortest_path(M, step, A, B):
    """
    The function for finding the shortest path (A-star)
    """
    rows, cols = np.shape(M)

    start = A
    end = B

    distances = np.full((rows, cols), np.inf, dtype=float64)
    distances[start] = 0.0

    previous_vertices = np.full((rows, cols, 2), -1, dtype=int64)

    vertices = [(0.0 + heuristic(start, end, step), start[0], start[1])]

    while vertices:
        _, current_row, current_col = heapq.heappop(vertices)

        for neighbor_row, neighbor_col in get_neighbors(current_row, current_col, rows, cols):
            height_diff = abs(M[current_row, current_col] - M[neighbor_row, neighbor_col])
            new_distance = distances[current_row, current_col] \
+ calculate_distance(height_diff, step)

            if new_distance < distances[neighbor_row, neighbor_col]:
                distances[neighbor_row, neighbor_col] = new_distance
                previous_vertices[neighbor_row, neighbor_col, 0] = current_row
                previous_vertices[neighbor_row, neighbor_col, 1] = current_col
                heapq.heappush(vertices, (new_distance + \
heuristic((neighbor_row, neighbor_col), end, step), neighbor_row, neighbor_col))

    path = []
    current_vertex = end
    while not np.all(previous_vertices[current_vertex[0], \
current_vertex[1]] == -1):
        path.append((current_vertex[0], current_vertex[1]))
        current_vertex = (previous_vertices[current_vertex[0], \
current_vertex[1], 0], previous_vertices[current_vertex[0], current_vertex[1], 1])

    path.append((start[0], start[1]))
    return path[::-1]
