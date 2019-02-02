from __future__ import absolute_import, unicode_literals
from celery import shared_task
import numpy as np

@shared_task
def get_determinant():
    matrix = np.array([[1, 2], [3, 4]])
    det = int(np.linalg.det(matrix))
    return det
