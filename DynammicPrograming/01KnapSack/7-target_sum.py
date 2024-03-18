"""
Target Sum = Count of subsets with a given difference
S1 = all elements with positive signs
S2 = all elements with negative signs

S1 - S2 = Sum
S1 + S2 = TotalSum
S1 = (Sum + TotalSum) // 2
"""

def subset_sum_possible(nums, total):
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
    return dp[-1][-1]

def target_sum(nums, total):
    total_sum = sum(nums)
    s1 = (total + total_sum) // 2
    return subset_sum_possible(nums, s1)

if __name__ == "__main__":
    arr = [1, 1, 1, 1]
    total = 2
    print(target_sum(arr, total)) # 4

    arr = [1, 2, 1]
    total = 0
    print(target_sum(arr, total)) # 2

