import sys

def min_amount_of_coins(amount, coins):
  coins.sort()
  dp = [[sys.maxsize if i>0 else 0 for j in coins] for i in range(amount+1)]

  for i in range(1, amount+1):
    for j in range(0, len(coins)):
      if i >= coins[j]:
        dp[i][j] = min(1 + dp[i - coins[j]][j], dp[i][j-1])
      else:
        dp[i][j] = dp[i][j-1]

  return dp[-1][-1]

coins = [3, 5, 8, 10]
for amount in range(41):
  print(amount, min_amount_of_coins(amount, coins))
