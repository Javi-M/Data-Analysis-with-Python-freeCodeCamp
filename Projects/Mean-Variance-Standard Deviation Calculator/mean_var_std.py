import numpy as np


def calculate(list):

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  matrix = np.reshape(np.array(list), (3, 3))
  axis1 = 0
  axis2 = 1

  calculations = {
    'mean': [np.mean(matrix, axis1).tolist(),\
             np.mean(matrix, axis2).tolist(),\
             np.mean(list)],
    'variance': [np.var(matrix, axis1).tolist(),\
                 np.var(matrix, axis2).tolist(),\
                 np.var(list)],
    'standard deviation': [np.std(matrix, axis1).tolist(),\
                           np.std(matrix, axis2).tolist(),\
                           np.std(list)],
    'max': [np.max(matrix, axis1).tolist(),\
            np.max(matrix, axis2).tolist(),\
            np.max(list)],
    'min': [np.min(matrix, axis1).tolist(),\
            np.min(matrix, axis2).tolist(),\
            np.min(list)],
    'sum': [np.sum(matrix, axis1).tolist(),\
            np.sum(matrix, axis2).tolist(),\
            np.sum(list)]
  }

  return calculations
