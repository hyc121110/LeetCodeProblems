'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

def minPathSum(grid):
    # get row size
    m = len(grid)
    # get col size
    n = len(grid[0])
    # init m x n return array with top left val as base case
    arr = [[grid[0][0] for _ in range(n)] for _ in range(m)]
    # base case: fill sum of grid[i][0] and grid[0][j]
    # row
    for i in range(1,n):
        arr[0][i] = grid[0][i] + arr[0][i-1]
    # col
    for i in range(1,m):
        arr[i][0] = grid[i][0] + arr[i-1][0]

    # fill the rest of the array
    for i in range(1,m):
        for j in range(1,n):
            # compare between the value above and on the right
            # if top val < left val -> choose top val
            if arr[i-1][j] < arr[i][j-1]:
                arr[i][j] = arr[i-1][j] + grid[i][j]
            else:
                arr[i][j] = arr[i][j-1] + grid[i][j]

    return arr[m-1][n-1]

print(minPathSum(grid=[[4,3,4,10],
                        [3,6,7,1],
                        [7,4,1,8]]))