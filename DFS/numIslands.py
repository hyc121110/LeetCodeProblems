'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def numIslands(grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                count += 1
    return count

def dfs(grid, i, j):
    # either out of the grid or not an island
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = '#'
    list(map(dfs, (grid, grid, grid, grid), (i-1, i+1, i, i), (j, j, j-1, j+1)))
    # dfs(grid, i+1, j) # move down one row
    # dfs(grid, i-1, j) # move up one row
    # dfs(grid, i, j+1) # move right one col
    # dfs(grid, i, j-1) # move left one col
    
grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]
print(numIslands(grid))