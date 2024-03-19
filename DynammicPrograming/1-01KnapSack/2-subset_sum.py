'''
Subset Sum Problem
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
'''
from typing import List

def subset_sum(nums: List[int], total: int) -> bool:
    n: int = len(nums)

    def subset_sum_util(nidx: int, wt: int) -> bool:
        if wt == 0:
            return True
        elif nidx == 0:
            return False
        elif nums[nidx - 1] <= wt:
            return subset_sum_util(nidx-1, wt) or subset_sum_util(nidx-1, wt-nums[nidx-1])
        else:
            return subset_sum_util(nidx-1, wt)
    return subset_sum_util(n, total)

def subset_sum_memo(nums: List[int], total: int) -> bool:
    n: int = len(nums)
    dp = [
        [-1 for _ in range(total + 1)]
        for _ in range(n + 1)
    ]
    def subset_sum_util(nidx: int, wt: int) -> bool:
        if wt == 0:
            return True
        elif nidx == 0:
            return False
        if dp[nidx][wt] != -1:
            return dp[nidx][wt]
        elif nums[nidx - 1] <= wt:
            dp[nidx][wt] = subset_sum_util(nidx - 1, wt) or subset_sum_util(nidx - 1, wt - nums[nidx - 1]) 
        else:
            dp[nidx][wt] = subset_sum_util(nidx - 1, wt)
        return dp[nidx][wt]
    subset_sum_util(n, total)
    for row in dp:
        print(row)
    return dp[n][total]

def subset_sum_topdown(nums: List[int], total: int) -> bool:
    n: int = len(nums)
    dp = [
        [-1 for _ in range(total + 1)]
        for _ in range(n + 1)
    ]
    for nidx in range(n + 1):
        for wt in range(total + 1):
            if wt == 0:
                dp[nidx][wt] = True
            elif nidx == 0:
                dp[nidx][wt] = False
            elif nums[nidx - 1] <= wt:
                dp[nidx][wt] = dp[nidx - 1][wt] or dp[nidx - 1][wt - nums[nidx - 1]]
            else:
                dp[nidx][wt] = dp[nidx - 1][wt]
    for row in dp:
        print(row)
    return dp[n][total]

if __name__ == "__main__":
    arr = [1, 2, 3, 2]
    total = 4
    
    # print(subset_sum(arr, total)) # True
    # print(subset_sum_memo(arr, total)) # True
    # print(subset_sum_topdown(arr, total)) # True
    print(subset_sum_topdown([1, 6, 11, 5], 23))