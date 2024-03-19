def rod_cutting_profit(prices, length):
    dp = [
        [0 for _ in range(len(length) + 1)]
        for _ in range(len(prices) + 1)
    ]
    for n in range(len(prices) + 1):
        for wt in range(len(length) + 1):
            if n == 0 or wt == 0:
                dp[n][wt] = 0
            elif length[n - 1] <= wt:
                dp[n][wt] = max(dp[n - 1][wt], prices[n - 1] + dp[n][wt - length[n - 1]])
            else:
                dp[n][wt] = dp[n - 1][wt]
    
    for row in dp:
        print(row)
    return dp[len(prices)][len(length)]

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    length = [1, 2, 3, 4, 5, 6, 7, 8]
    print(rod_cutting_profit(prices, length)) # 22

    prices = [5, 6, 8, 8]
    length = [1, 2, 3, 4]
    print(rod_cutting_profit(prices, length)) # 10