'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
'''

# standard longest common substring dynamic programming solution
def findLength(A, B):
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    max_val = 0
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_val = max(max_val, dp[i][j])
    return max_val

A=[1,2,3,2,1]
B=[3,2,1,4,7]
print(findLength(A, B))