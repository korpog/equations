import numpy as np
import copy


def solve(matrix, b_vals):
    det_main = get_determinant(matrix)
    if det_main == 0:
        return {'det_zero': 'The determinant of the matrix is equal to zero. Cannot solve.'}
    solutions = {}
    for i in range(len(b_vals)):
        mtrx = copy.copy(matrix)
        swap_column(mtrx, i, b_vals)
        det = get_determinant(mtrx)
        solution = round(det / det_main, 2)
        solutions[f'x_{i + 1}'] = solution
    return solutions


def swap_column(matrix, col_index, b_vals):
    matrix[:, col_index] = b_vals


def get_determinant(matrix):
    det = np.linalg.det(matrix)
    return det
