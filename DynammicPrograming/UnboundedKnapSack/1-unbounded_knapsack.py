import unittest

def unbounded_knapsack(weights, values, capacity):
    def unbounded_knapsack_util(n, wt):
        if n == 0 or wt == 0:
            return 0
        elif weights[n - 1] <= wt:
            return max(unbounded_knapsack_util(n - 1, wt),
                       values[n - 1] + unbounded_knapsack_util(n, wt - weights[n - 1]))
        else:
            return unbounded_knapsack_util(n - 1, wt)
    return unbounded_knapsack_util(len(weights), capacity)

def unbounded_knapsack_memoisation(weights, values, capacity):
    dp = [
        [-1 for _ in range(capacity + 1)]
        for _ in range(len(weights) + 1)
    ]
    def unbounded_knapsack_util(n, wt):
        if n == 0 or wt == 0:
            return 0
        elif dp[n][wt] != -1:
            return dp[n][wt]
        elif weights[n - 1] <= wt:
            dp[n][wt] = max(unbounded_knapsack_util(n - 1, wt),
                            values[n - 1] + unbounded_knapsack_util(n, wt - weights[n - 1]))
        else:
            dp[n][wt] = unbounded_knapsack_util(n - 1, wt)
        return dp[n][wt]
    return unbounded_knapsack_util(len(weights), capacity)

def unbounded_knapsack_topdown(weights, values, capacity):
    dp = [
        [-1 for _ in range(capacity + 1)]
        for _ in range(len(weights) + 1)
    ]
    for n in range(len(values) + 1):
        for wt in range(capacity + 1):
            if n == 0 or wt == 0: dp[n][wt] = 0
            elif weights[n - 1] <= wt:
                dp[n][wt] = max(
                    dp[n - 1][wt],
                    values[n - 1] + dp[n][wt -weights[n - 1]]
                )
            else: dp[n][wt] = dp[n - 1][wt]
    return dp[-1][-1]



class TestUnboundedKnapsack(unittest.TestCase):
    def setUp(self) -> None:
        self.testcases = [
            (([1, 2, 3, 5], [1, 5, 4, 8], 6), 15)
        ]
    def test_unbounded_knapsack(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                actual = unbounded_knapsack(*args)
                self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
    
    def test_unbounded_knapsack_memoisation(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                actual = unbounded_knapsack_memoisation(*args)
                self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
    
    def test_unbounded_knapsack_topdown(self):
        for args, expected in self.testcases:
            with self.subTest(args=args, expected=expected):
                actual = unbounded_knapsack_topdown(*args)
                self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

if __name__ == "__main__":
    unittest.main()
        
       