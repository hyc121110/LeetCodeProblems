'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''

def pascalTriangle(numRows):
  res = list()
  for i in range(numRows):
    temp = list()
    temp.append(1)
    for j in range(1, i):
      temp.append(res[i-1][j-1]+res[i-1][j])
    if i > 0:
      temp.append(1)
    res.append(temp)
  return res

print(pascalTriangle(0))