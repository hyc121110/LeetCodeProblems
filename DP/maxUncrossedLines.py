'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j], 
and the line we draw does not intersect any other connecting (non-horizontal) line.

Return the maximum number of connecting lines we can draw in this way.
'''

# dynamic programming 2d array (longest common subsequence)
from collections import defaultdict

def maxUncrossedLines(A, B):
    dp, m, n = defaultdict(int), len(A), len(B)

    for i in range(m):
        for j in range(n):
            dp[i,j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
    return dp[m - 1, n - 1]


A = [2,5,1,2,5]
B = [10,5,2,1,5,2]
print(maxUncrossedLines(A, B))