from typing import List


def subset_sum(nums: List[int], total: int) -> int:
    def subset_sum_util(n: int, wt: int) -> int:
        if wt == 0:
            return 1
        elif n == 0:
            return 0
        elif nums[n-1] <= wt:
            return subset_sum_util(n-1, wt) + subset_sum_util(n-1, wt - nums[n-1])
        else:
            return subset_sum_util(n-1, wt)
    return subset_sum_util(len(nums), total)

def subset_sum_memoization(nums: List[int], total: int) -> int:
    dp = [
        [-1 for _ in range(total + 1)]
        for _ in range(len(nums) + 1)
    ]
    def subset_sum_util(n: int, wt: int) -> int:
        if wt == 0:
            return 1
        elif n == 0:
            return 0
        elif dp[n][wt] != -1:
            return dp[n][wt]
        elif nums[n-1] <= wt:
            dp[n][wt] = subset_sum_util(n-1, wt) + subset_sum_util(n-1, wt - nums[n-1])
        else:
            dp[n][wt] = subset_sum_util(n-1, wt)
        return dp[n][wt]
    return subset_sum_util(len(nums), total)

def subset_sum_topdown(nums: List[int], total: int) -> int:
    dp = [
        [-1 for _ in range(total + 1)]
        for _ in range(len(nums) + 1)
    ]
    for n in range(len(nums)+1):
        for wt in range(total+1):
            if wt == 0: dp[n][wt] = 1
            elif n == 0: dp[n][wt] = 0
            elif nums[n-1] <= wt: dp[n][wt] = dp[n-1][wt] + dp[n-1][wt - nums[n-1]]
            else: dp[n][wt] = dp[n-1][wt]
    for row in dp:
        print(row)
    return dp[len(nums)][total]

if __name__ == "__main__":
    # nums = [2, 3, 5, 6, 8, 10]
    # total = 10
    # print(subset_sum(nums, total))
    # print(subset_sum_memoization(nums, total))
    # print(subset_sum_topdown(nums, total))
    nums = [1, 1, 2, 3]
    total = 7
    print(subset_sum_topdown(nums, total))
