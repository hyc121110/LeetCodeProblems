'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''

'''
Store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.
'''

def setZeros(matrix):
  m = len(matrix)
  n = len(matrix[0])
  col0 = True
  
  for i in range(m):
    if matrix[i][0] == 0: col0 = False
    for j in range(1, n):
      if matrix[i][j] == 0:
        matrix[i][0] = matrix[0][j] = 0

  for i in range(m-1, -1, -1):
    for j in range(n-1, 0, -1):
      if matrix[i][0] == 0 or matrix[0][j] == 0:
        matrix[i][j] = 0
    if not col0: matrix[i][0] = 0

matrix = \
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

print(setZeros(matrix))
print(matrix)