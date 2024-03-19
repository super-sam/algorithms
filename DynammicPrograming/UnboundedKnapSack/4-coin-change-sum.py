from __future__ import print_function

"""
Find number of ways coin can be selected to get the sum
"""

def coin_change(coins, amount):
    def coin_change_util(n, amt):
        if amt == 0:
            return 1
        elif n == 0:
            return 0
        elif coins[n - 1] <= amt:
            included = coin_change_util(n, amt - coins[n - 1])
            excluded = coin_change_util(n -1, amt)
            return included + excluded
        else:
            return coin_change_util(n -1, amt)
    
    return coin_change_util(len(coins), amount)

def coin_change_memoisation(coins, amount):
    dp = [
       [-1 for _ in range(amount + 1)]
       for _ in range(len(coins) + 1)
    ]
    def coin_change_util(n, amt):
        if amt == 0:
            return 1
        elif n == 0:
            return 0
        elif dp[n][amt] != -1:
            return dp[n][amt]
        elif coins[n - 1] <= amt:
            included = coin_change_util(n, amt - coins[n - 1])
            excluded = coin_change_util(n - 1, amt)
            dp[n][amt] = included + excluded
        else:
            dp[n][amt] = coin_change_util(n - 1, amt)
        return dp[n][amt]
    return coin_change_util(len(coins), amount) 

def coin_change_bottom_up(coins, amount):
  # replace this placeholder return statement with your code
  dp = [
    [-1 for _ in range(amount + 1)]
    for _ in range(len(coins) + 1)
  ]
  for csize in range(len(coins) + 1):
    for amt in range(amount + 1):
      if amt == 0:
        dp[csize][amt] = 1
      elif csize == 0:
        dp[csize][amt] = 0
      elif coins[csize - 1] <= amt:
        dp[csize][amt] = dp[csize - 1][amt] + dp[csize][amt - coins[csize - 1]]
      else:
        dp[csize][amt] = dp[csize - 1][amt]
  return dp[-1][-1]

def coin_change_1d(coins, amount):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for amt in range(1, amount + 1):
        for coin in coins:
            if amt < coin:
               continue
            dp[amt] += dp[amt - coin]
            print(coin, amt, dp)
    
    return dp[amount]

if __name__ == "__main__":
    # coins = [1, 2, 5]
    # amount = 7
    coins = [1, 3, 4]
    amount = 4
    print(coin_change(coins, amount)) # 6
    print(coin_change_memoisation(coins, amount)) # 6
    print(coin_change_bottom_up(coins, amount)) # 6
    print(coin_change_1d(coins, amount)) # 6