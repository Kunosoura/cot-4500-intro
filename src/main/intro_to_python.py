import numpy as np

# Prints the 2d matrix in the format required by the assignment. Only pretty for
#    matrices where all the elements have the same number of digits
def printMatrixPretty(matrix_2d):
  for i in range(len(matrix_2d)):
    for j in range(len(matrix_2d[0])):
      print(matrix_2d[i][j], end=' ')
    print()
  print()

# 1: Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
#    I generate the elements as a function of i and j
myMatrix = np.fromfunction(lambda i, j: (i == j) * 1, (3,3), dtype=int)
printMatrixPretty(myMatrix)

# 2: Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j
#    Again I generate the elements of the new array used in the summation as
#    a function of i and j
myMatrix += np.fromfunction(lambda i, j: (i != j) * 3 , (3,3), dtype=int)
printMatrixPretty(myMatrix)

# 3: Print the 3x3 matrix from #2 as a 3x2 by deleting 
#    the last column from the matrix created
#    Here I just reassign the matrix to a slice of itself
myMatrix = myMatrix[:3,:2]
printMatrixPretty(myMatrix)
