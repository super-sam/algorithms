from typing import List

def knapsack(wt: List[int], val: List[int], capacity: int) -> int:
    n: int = len(wt)
    def knapsack_util(capacity: int, nsize: int) -> int:
        if capacity == 0 or nsize == 0:
            return 0
        if wt[nsize - 1] <= capacity:
            return max(knapsack_util(capacity, nsize - 1), 
                       val[nsize - 1] + knapsack_util(capacity - wt[nsize - 1], nsize - 1))
        else:
            return knapsack_util(capacity, nsize - 1)
    return knapsack_util(capacity, n)

def knapsack_memoisation(wt: List[int], val: List[int], capacity: int) -> int:
    n: int = len(wt)
    dp = [
        [-1 for _ in range(capacity + 1)]
        for _ in range(n + 1)
    ]
    def knapsack_util(capacity: int, nsize: int) -> int:
        if capacity == 0 or nsize == 0:
            return 0
        
        if dp[nsize][capacity] != -1:
            return dp[nsize][capacity]
        
        if wt[nsize - 1] <= capacity:
            dp[nsize][capacity] = max(knapsack_util(capacity, nsize - 1), 
                                      val[nsize-1] + knapsack_util(capacity - wt[nsize - 1], nsize - 1))
        else:
            dp[nsize][capacity] = knapsack_util(capacity, nsize - 1)
        return dp[nsize][capacity]
    
    knapsack_util(capacity, n)
    from pprint import pprint
    pprint(dp)
    return dp[n][capacity]

def knapsack_topdown(wt: List[int], val: List[int], capacity: int) -> int:
    n: int = len(wt)
    dp = [
        [-1 for _ in range(capacity + 1)]
        for _ in range(n + 1)
    ]
    for nsize in range(n + 1):
        for cap in range(capacity + 1):
            if nsize == 0 or cap == 0:
                dp[nsize][cap] = 0
                continue
            if wt[nsize - 1] <= cap:
                dp[nsize][cap] = max(dp[nsize - 1][cap], 
                                     val[nsize - 1] + dp[nsize - 1][cap - wt[nsize - 1]])
            else:
                dp[nsize][cap] = dp[nsize - 1][cap]
    from pprint import pprint
    pprint(dp)
    return dp[n][capacity]
if __name__ == "__main__":
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]
    w = 7
    assert knapsack(wt, val, w) == 9, "Failed"
    print(knapsack(wt, val, w))  # 9
    # assert knapsack_memoisation(wt, val, w) == 9, "Failed"
    print(knapsack_memoisation(wt, val, w))  # 9
    assert knapsack_topdown(wt, val, w) == 9, "Failed"
    print(knapsack_topdown(wt, val, w))  # 9