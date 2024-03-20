import unittest


def coin_change_min(coins, amount):
    def coin_change_min_util(amt, n):
        if amt == 0:
            return 0
        elif n == 0:
            return float("inf")
        elif coins[n-1] <= amt:
            return min(coin_change_min_util(amt, n-1), 
                       1 + coin_change_min_util(amt - coins[n - 1], n))
        else:
            return coin_change_min_util(amt, n-1)
    
    return coin_change_min_util(amount, len(coins))

def coin_change_min_memoisation(coins, amount):
    dp = [
        [-1 for _ in range(amount + 1)]
        for _ in range(len(coins) + 1)
    ]
    def coin_change_min_util(amt, n):
        if amt == 0:
            return 0
        elif n == 0:
            return float("inf")
        
        if dp[n][amt] != -1:
            return dp[n][amt]
        
        if coins[n - 1] <= amt:
            dp[n][amt] = min(coin_change_min_util(amt, n-1), 
                             1 + coin_change_min_util(amt - coins[n - 1], n))
        else:
            dp[n][amt] = coin_change_min_util(amt, n - 1)
    
    return coin_change_min_util(amount, len(coins))

def coin_change_min_topdown(coins, amount):
    dp = [
        [-1 for _ in range(amount + 1)]
        for _ in range(len(coins) + 1)
    ]
    for n in range(len(coins) + 1):
        for amt in range(amount + 1):
            if amt == 0:
                dp[n][amt] = 0
            elif n == 0:
                dp[n][amt] = float("inf")
            elif coins[n - 1] <= amt:
                dp[n][amt] = min(dp[n - 1][amt],
                                 1 + dp[n][amt - coins[n - 1]])
            else:
                dp[n][amt] = dp[n - 1][amt]
    return dp[len(coins)][amount]

def denomination(currency, count, amount):
    currencies = []
    for i in range(len(currency)):
        currencies.extend([currency[i]]*count[i])
    
    def denomination_util(amt, n):
        if amt == 0:
            return 0
        elif n == 0:
            return float("inf")
        elif currencies[n - 1] <= amt:
            return min(denomination_util(amt, n - 1),
                       1 + denomination_util(amt - currencies[n - 1], n - 1))
        else:
            return denomination_util(amt, n - 1)
    return denomination_util(amount, len(currencies))

class TestMinCoinSum(unittest.TestCase):
    def setUp(self) -> None:
        self.testcases = [
            (([1, 2, 5], 11), 3),
            (([2], 3), float("inf"))
        ]
    def test_generic(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                self.assertEqual(coin_change_min(*args), expected)
    
    def test_memoisation(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                self.assertEqual(coin_change_min(*args), expected)
    def test_topdown(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                self.assertEqual(coin_change_min(*args), expected)

class TestDenomination(unittest.TestCase):
    def setUp(self) -> None:
        self.testcases = [
            (([10, 20, 50, 100], [5, 2, 2, 2], 90), 3),
            (([10, 20, 50, 100], [5, 1, 2, 2], 90), 4)
        ]
    def test_generic(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                self.assertEqual(denomination(*args), expected)
if __name__ == "__main__":
    unittest.main()