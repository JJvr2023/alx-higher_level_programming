#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  """Computes the square value of all integers of a matrix.

  Args:
    matrix: A 2 dimensional array.

  Returns:
    A new matrix:
      Same size as matrix
      Each value should be the square of the value of the input
    Initial matrix should not be modified

  Raises:
    ValueError: If matrix is not a 2 dimensional array.
  """

  if not isinstance(matrix, list):
    raise ValueError("matrix must be a 2 dimensional array")

  if len(matrix) == 0:
    return []

  if len(matrix[0]) == 0:
    return []

  new_matrix = []
  for row in matrix:
    new_row = []
    for value in row:
      new_row.append(value ** 2)
    new_matrix.append(new_row)

  return new_matrix
