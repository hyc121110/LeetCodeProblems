'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
'''

def coinChange(coins, amount):
  dp = [0] + [float('inf') for i in range(amount)]
  for i in range(1, amount+1):
    for coin in coins: # check every coin to see if it is possible to reach the amount
      if i - coin >= 0: # only check if the amount is larger than the coin value, because if coin is smaller value, it is impossible to reach the amount
        # find the min between the original minimum number by reaching the sum directly or below
        # dp[i-coin]+1 representing the number of coins needed from the previous sum plus the coin (1) itself (because (i-val(coin))+val(coin) = i)
        dp[i] = min(dp[i], dp[i-coin] + 1)
  if dp[-1] == float('inf'):
    return -1
  return dp[-1]

print(coinChange(coins = [1, 2, 5], amount = 11))

# time complexity: O(n*w), w is the amount, n is the size of coins
# space complexity: O(w), size of dp depends on amount