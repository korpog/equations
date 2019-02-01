import numpy as np


def get_determinant():
    matrix = np.array([[1, 2], [3, 4]])
    det = int(np.linalg.det(matrix))
    return det
