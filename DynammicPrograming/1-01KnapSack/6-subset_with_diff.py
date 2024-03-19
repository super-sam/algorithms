"""
s1 - s2 = diff
s1 + s2 = total
----------------
2s1 = total + diff
s1 = (total + diff) // 2
"""

def subset_possible_count(nums, total):
    dp = [
        [0 for _ in range(total + 1)]
        for _ in range(len(nums) + 1)
    ]
    for n in range(len(nums) + 1):
        for wt in range(total + 1):
            if wt == 0: dp[n][wt] = 1
            elif n == 0: dp[n][wt] = 0
            elif nums[n-1] <= wt: dp[n][wt] = dp[n-1][wt] + dp[n-1][wt - nums[n-1]]
            else: dp[n][wt] = dp[n-1][wt]
    return dp[n][total]

def subset_with_diff(nums, diff):
    total = sum(nums)
    s1 = (total + diff)//2
    return subset_possible_count(nums, s1)

if __name__ == "__main__":
    arr = [1, 1, 2, 3]
    diff = 1
    print(subset_with_diff(arr, diff)) # 3
    arr = [1, 2, 7]
    diff = 4
    print(subset_with_diff(arr, diff)) # 1
    