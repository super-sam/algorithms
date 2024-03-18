from typing import List

def sumset_sum_possible(nums: List[int], total: int) -> List[bool]:
    dp = [
        [False for _ in range(total + 1)]
        for _ in range(len(nums) + 1)
    ]
    for n in range(len(nums) + 1):
        for wt in range(total + 1):
            if wt == 0: dp[n][wt] = True
            elif n == 0: dp[n][wt] = False
            elif nums[n-1] <= wt: dp[n][wt] = dp[n-1][wt] or dp[n-1][wt - nums[n-1]]
            else: dp[n][wt] = dp[n-1][wt]
    return dp[len(nums)]

def min_subset_diff(nums: List[int]) -> int:
    total = sum(nums)
    subsets = sumset_sum_possible(nums, total)
    # left = total // 2
    # right = left if total % 2 == 0 else left + 1
    # while left >=0:
    #     if subsets[left] and subsets[right]:
    #         return right - left
    #     left -= 1
    #     right += 1
    has_subset = [i for i, v in enumerate(subsets) if v]
    print(has_subset)
    return total - 2 * has_subset[(len(has_subset) -1) // 2] 
    

if __name__ == "__main__":
    arr = [45,2,9,87,9,12,54,56]
    print(min_subset_diff(arr)) # 6