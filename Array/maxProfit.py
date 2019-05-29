def maxProfit(prices):
  # max_cur tracks the difference of max[i] and future max[i]s
  max_cur = max_so_far = 0

  for i in range(1, len(prices)):
    # record the difference
    max_cur += prices[i] - prices[i-1]
    # as soon as max_cur is negative, reset max_cur to 0
    max_cur = max(0, max_cur)
    max_so_far = max(max_cur, max_so_far)

  return max_so_far

print(maxProfit(prices=[7,1,5,3,6,4]))