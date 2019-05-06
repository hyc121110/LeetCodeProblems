'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

def uniquePaths(m, n):
    # Space can be reduced to O(n) with only one row
    cur = [1 for _ in range(n)]
    # start from index 1 as we already initialized base cases
    for _ in range(1,m):
        for j in range(1,n):
            # previous cur[j] is the value on the left on 2d array
            # updating cur[j] using the old cur[j] (same row) and
            # the value on the previous row
            cur[j] += cur[j-1]
    # return the destination block 
    return cur[n-1]

print(uniquePaths(m=4,n=5))