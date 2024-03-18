'''
if total sum is odd then not possible
if total sum is even then check if there is a subset with sum = total sum / 2
'''

from typing import List

def equal_sum(nums: List[int]) -> bool:
    if sum(nums) % 2 != 0:
        return False
    def equal_sum_util(n: int, wt: int) -> bool:
        if wt == 0:
            return True
        elif n == 0:
            return False
        elif nums[n-1] <= wt:
            return equal_sum_util(n-1, wt) or equal_sum_util(n-1, wt - nums[n-1])
        else:
            return equal_sum_util(n-1, wt)
    
    return equal_sum_util(len(nums), sum(nums) // 2)

def equal_sum_memoization(nums: List[int]) -> bool:
    if sum(nums) % 2 != 0:
        return False
    dp = [
        [-1 for _ in range(sum(nums) // 2 + 1)]
        for _ in range(len(nums) + 1)
    ]
    def equal_sum_util(n: int, wt: int) -> bool:
        if wt == 0:
            return True
        elif n == 0:
            return False
        if dp[n][wt] != -1:
            return dp[n][wt]
        elif nums[n-1] <= wt:
            dp[n][wt] = equal_sum_util(n-1, wt) or equal_sum_util(n-1, wt - nums[n-1])
        else:
            dp[n][wt] = equal_sum_util(n-1, wt)
        return dp[n][wt]
    return equal_sum_util(len(nums), sum(nums) // 2)