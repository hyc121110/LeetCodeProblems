'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
'''

def numTrees(n):
    # init array of size n+1 for storing
    dp = [0] * (n+1)

    # base cases
    dp[0] = 1
    dp[1] = 1

    # F(i, n) = G(n-i) * G(i-1)
    for level in range(2, n+1):
        for i in range(1, level+1):
            dp[level] += dp[level-i] * dp[i-1]
    return dp[n]

print(numTrees(n=3))