import functools

from typing import List

def has_subset(nums: List[int], target: int) -> bool:
    dp = [
        [None for _ in range(target + 1)]
        for _ in range(len(nums) + 1)
    ]
    for n in range(len(dp)):
        for w in range(dp[0]):
            if w == 0:
                dp[n][w] = True
            elif n == 0:
                dp[n][w] = False
            elif nums[n-1] < w:
                dp[n][w] = dp[n-1][w] or dp[n-1][w - num[n-1]]
            else:
                dp[n][w] = dp[n-1][w]
    return dp[n][w]