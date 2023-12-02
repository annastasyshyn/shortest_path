"""Project"""
import math


def read(file_path: str) -> list[list[int]]:
    """Read data from csv file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    matrix = [[int(i) for i in j.split(',')] for j in data.strip().split('\n')]
    return matrix

def matrix_to_graph(matrix: list[list[int]]) -> dict:
    """Turn matrix into a graph"""
    graph = {}
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            vertex = (i, j)
            graph[vertex] = []
            if i > 0:
                graph[vertex].append((i - 1, j))
            if i < rows - 1:
                graph[vertex].append((i + 1, j))
            if j > 0:
                graph[vertex].append((i, j - 1))
            if j < cols - 1:
                graph[vertex].append((i, j + 1))
    return graph

def distance(point_a: tuple[int], point_b: tuple[int], step: int, matrix: list[list[int]]):
    """-"""
    height_difference = abs(matrix[point_a[0]][point_a[1]] - matrix[point_b[0]][point_b[1]])
    physical_distance = math.sqrt((point_a[0] \
- point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) * step
    edge_weight = math.sqrt(height_difference ** 2 + physical_distance ** 2)
    return edge_weight


# print(matrix_to_graph(read('/home/Anya/UCU/pb/discrete_maths_project/example.csv')))
# print(distance((0,0), (2,2), 1, read('/home/Anya/UCU/pb/discrete_maths_project/example.csv')))
