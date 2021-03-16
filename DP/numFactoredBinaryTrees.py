"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.
"""

"""
My t[a] tells the number of trees with root value a. The 1 is for making a leaf (there's one way to make a leaf with that value), the sum is for non-leaves (go over every possible left child value b).
"""
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        for a in sorted(arr):
            dp[a] = sum(dp[b] * dp.get(a / b, 0) for b in dp if a % b == 0) + 1
        return sum(dp.values()) % (10**9 + 7)