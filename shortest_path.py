import heapq
import random
from typing import List, Tuple, Optional


def generate_random_matrix(rows: int, cols: int, max_value: int = 10) -> List[List[int]]:
    """
    Generates a matrix with random values between 1 and max_value.

    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        max_value (int): Maximum value of elements in the matrix (default is 10).

    Returns:
        List[List[int]]: A matrix filled with random values.
    """
    return [[random.randint(1, max_value) for _ in range(cols)] for _ in range(rows)]


def dijkstra(matrix: List[List[int]]) -> Tuple[List[List[float]], List[List[Optional[Tuple[int, int]]]]]:
    """
    Finds the shortest path in a matrix using Dijkstra's algorithm.

    Args:
        matrix (List[List[int]]): The input matrix with weights.

    Returns:
        Tuple[List[List[float]], List[List[Optional[Tuple[int, int]]]]]:
            - distances: Matrix with shortest distances from the top-left to each cell.
            - path_matrix: Matrix used to reconstruct the shortest path.
    """
    rows, cols = len(matrix), len(matrix[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = matrix[0][0]
    priority_queue = [(matrix[0][0], 0, 0)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path_matrix = [[None] * cols for _ in range(rows)]

    while priority_queue:
        current_distance, x, y = heapq.heappop(priority_queue)

        if x == rows - 1 and y == cols - 1:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                distance = current_distance + matrix[nx][ny]
                if distance < distances[nx][ny]:
                    distances[nx][ny] = distance
                    heapq.heappush(priority_queue, (distance, nx, ny))
                    path_matrix[nx][ny] = (x, y)

    return distances, path_matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints the matrix to the console.

    Args:
        matrix (List[List[int]]): The matrix to print.
    """
    for row in matrix:
        print(row)


# Parameters for the matrix
rows, cols = 5, 5
max_value = 10

# Generate and display a random matrix
matrix = generate_random_matrix(rows, cols, max_value)
print("Randomly generated matrix:")
print_matrix(matrix)

# Find the shortest path
distances, path_matrix = dijkstra(matrix)
print("\nShortest path distances matrix:")
print_matrix(distances)

# Reconstruct the shortest path
shortest_path = []
x, y = rows - 1, cols - 1
while (x, y) != (0, 0):
    shortest_path.append((x, y))
    x, y = path_matrix[x][y]
shortest_path.append((0, 0))
shortest_path.reverse()

