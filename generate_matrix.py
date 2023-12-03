"""Generate csv file for testing"""
import random


def generate_csv(n, filename):
    """-"""
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    with open(filename, 'w', encoding='utf-8') as file:
        for row in matrix:
            row_str = ','.join(map(str, row))
            file.write(row_str + '\n')

generate_csv(5000, 'matr2.csv')
