def numIslands2(A):
    # idea: convert all 1s on the edge and 1s connected to the edge to 0 
    # and count the number of remaining ones
    def dfs(row, col):
        # out of range or not "land"
        if row < 0 or row == len_row or col < 0 or col == len_col or A[row][col] != 1:
            return
        # convert 1 to 0
        A[row][col] = 0
        
        # do this function for four other directions
        list(map(dfs, (row-1, row+1, row, row), (col, col, col-1, col+1)))
        # dfs(row-1, col)
        # dfs(row+1, col)
        # dfs(row, col-1)
        # dfs(row, col+1)
            
    if not A:
        return 0
    
    len_row = len(A)
    len_col = len(A[0])
    
    for row in range(len_row):
        for col in range(len_col):
            if A[row][col] == 1 and (row == 0 or col == 0 or row == len_row - 1 or col == len_col - 1):
                dfs(row, col)
    return sum(sum(row) for row in A) # summing each row in the grid
        
# grid = [[0,1,1,0],
#         [0,0,1,0],
#         [0,0,1,0],
#         [0,0,0,0]]
grid = [[0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]]
print(numIslands2(grid))