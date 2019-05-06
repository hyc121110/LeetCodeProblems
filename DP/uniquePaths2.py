'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
'''

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    # method 1: the obvious solution
    # initialize 2d array with size m+1 by n+1 to all 0 
    # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # # needed for the boundary cases
    # dp[0][1] = 1
    # # dp[1][0] = 1
    # for i in range(1, m+1):
    #     for j in range(1, n+1):
    #         if not obstacleGrid[i-1][j-1]:
    #            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # return dp[m][n]

    # method 2: optimized to O(n) space with only one list
    # each element of the list is the number of ways that
    # can get to the column with the row changes
    dp = [0 for _ in range(n)]

    # initialize first element for boundary cases
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j]:
                # set to 0 as impossible to go through
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    return dp[j-1]


obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0],
                [0,0,0]]

print(uniquePathsWithObstacles(obstacleGrid))