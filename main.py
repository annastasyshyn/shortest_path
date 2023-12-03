"""Project"""
import math
import heapq


def read(file_path: str) -> list[list[int]]:
    """Read data from csv file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return [[int(i) for i in j.split(',')] for j in data.strip().split('\n')]

def matrix_to_graph(matr: list[list[int]]) -> dict:
    """Turn matrix into a graph"""
    graph = {}
    rows, cols = len(matr), len(matr[0])
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

def calculate_distance(point_a: tuple[int], point_b: tuple[int], step: int, matrix: list[list[int]]):
    """-"""
    height_difference = abs(matrix[point_a[0]][point_a[1]] - matrix[point_b[0]][point_b[1]])
    physical_distance = math.sqrt((point_a[0] \
- point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) * step
    edge_weight = math.sqrt(height_difference ** 2 + physical_distance ** 2)
    return edge_weight

def dijkstra(graph, start, end, matr, step):
    """-"""
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            weight = calculate_distance(current_vertex, neighbor, step, matr)
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    path, current_vertex = [], end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = min(graph[current_vertex], key=lambda x: distances[x])

    path.insert(0, start)
    return path

matrix = read('/home/Anya/UCU/pb/discrete_maths_project/matr1.csv')
gr = matrix_to_graph(matrix)
a = (0,0)
b = (999,999)
STEP = 1
path = dijkstra(gr, a, b, matrix, STEP)
print(path)
