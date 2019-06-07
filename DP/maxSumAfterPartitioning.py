'''
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.
'''

def maxSumAfterPartitioning(A, K):
  # get length of A
  N = len(A)
  # initialize dp 
  dp = [0] * (N+1)
  # iterate through the list
  for i in range(N):
    cur_max = 0
    # iterate the previous k or i+1 values depends which is smaller and also itself
    for k in range(1, min(K, i+1) + 1):
      # the maximum value in the subarray
      cur_max = max(cur_max, A[i - k + 1])
      # if i < k: dp[i-k] = 0 -> only equal to cur_max*k
      # compare with different k to see which sum is the largest
      dp[i] = max(dp[i], dp[i - k] + cur_max * k)
  return dp[N-1]

print(maxSumAfterPartitioning(A=[1,15,7,9,2,5,10], K=3))