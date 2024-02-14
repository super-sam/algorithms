from typing import List

def has_subset(nums: List[int], target: int) -> bool:
    def has_subset_util(n: int, w: int) -> bool:
        if w == 0:
            return True
        if n == 0:
            return False
        if nums[n-1] <= w:
            return has_subset_util(n-1, w- nums[n-1]) or has_subset_util(n-1, w)
        else:
            return has_subset_util(n-1, w)
    return has_subset_util(len(nums), target)

def has_subset_memo(nums: List[int], target: int) -> bool:
    dp = [
        [None for _ in range(target+1)]
        for _ in range(len(nums)+1)
    ]
    def has_subset_util(n: int, w: int) -> bool:
        if w == 0:
            return True
        if n == 0:
            return False
        if dp[n][w] != None:
            return dp[n][w]
        
        if nums[n-1] <= w:
            dp[n][w] = has_subset_util(n-1, w- nums[n-1]) or has_subset_util(n-1, w)
        else:
            dp[n][w] = has_subset_util(n-1, w)
        
        return dp[n][w]
    return has_subset_util(len(nums), target)

def has_subset_dp(nums: List[int], target: int) -> bool:
    dp = [
        [False for _ in range(total+1)]
        for _ in range(len(nums) + 1)
    ]
    for n in range(len(dp)):
        for w in range(len(dp[0])):
            if w == 0:
                dp[n][w] = True
            elif n == 0:
                dp[n][w] = False
            elif nums[n-1] <= w:
                dp[n][w] = dp[n-1][w] or dp[n-1][w - nums[n-1]]
            else:
                dp[n][w] = dp[n-1][w]
    return dp[n][w]
if __name__ == "__main__":
    print(has_subset([2, 3, 7, 8, 10], 11))