"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""

# solution: similar to 0-1 knapsack problem, using 2d matrix to find the siz of the largest subset

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for str in strs:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # comparing between using the current number or the previous largest subset from previous i and j
                    # plus one (the current string)
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]