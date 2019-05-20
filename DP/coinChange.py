'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
'''

def coinChange(coins, amount):
  # Assume dp[i] is the fewest number of coins making up amount i
  MAX = float('inf')
  dp = [0] + [MAX] * amount

  for i in range(1, amount + 1):
    # for every coin in coins, dp[i] = min(dp[i - coin] + 1).
    dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

  # return dp[-1] (last value of the list) if dp[-1] != MAX else return -1
  return [dp[-1], -1][dp[-1] == MAX]

print(coinChange(coins = [1, 2, 5], amount = 11))