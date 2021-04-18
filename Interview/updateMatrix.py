# BFS
"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
"""
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        # first append all 0 cell to queue
        # using deque for faster popping
        q = deque()
        visited = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)] 
        while q:
            old_x, old_y = q.popleft()
            
            for item in direction:
                new_x, new_y = old_x+item[0], old_y+item[1]
                
                # limit coordinates to be within the matrix
                if new_x >= 0 and new_x < len(matrix) and new_y >= 0 and new_y < len(matrix[0]) and (new_x, new_y) not in visited:
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    q.append((new_x,new_y))
                    visited.add((new_x,new_y))

        return matrix