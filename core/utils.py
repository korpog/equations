import numpy as np


def solve(matrix, b_vals):
    det_main = get_determinant(matrix)
    solutions = []
    for i in range(len(b_vals)):
        matrix = swap_column(matrix, i, b_vals)
        det = get_determinant(matrix)
        solutions.append(det / det_main)
    return solutions

def swap_column(matrix, col_index, b_vals):
    matrix[:, col_index] = b_vals
    return matrix


def get_determinant(matrix):
    det = int(np.linalg.det(matrix))
    return det
