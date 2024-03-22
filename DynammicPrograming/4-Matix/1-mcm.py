import sys

def mcm(arr):
    def mcm_util(i, j):
        if i >= j:
            return 0
        temp = sys.maxsize
        for k in range(i, j):
            temp = min(temp, 
                       mcm_util(i, k) + 
                       mcm_util(k+1, j) + 
                       arr[i - 1] * arr[k] * arr[j]
                )
        return temp
    return mcm_util(1, len(arr) - 1)

def mem_memoisation(arr):
    dp = [
        [-1 for _ in range(len(arr))] 
        for _ in range(len(arr))
    ]
    def mcm_util(i, j):
        if i >= j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
    
        temp = sys.maxsize
        for k in range(i, j):
            temp = min(temp, 
                       mcm_util(i, k) + 
                       mcm_util(k+1, j) + 
                       arr[i - 1] * arr[k] * arr[j]
                )
        dp[i][j] = temp
        return dp[i][j]
    mcm_util(1, len(arr) - 1)
    for i in range(len(arr)):
        print(dp[i])
    return dp[1][len(arr) - 1]

if __name__ == '__main__':
    arr = [40, 20, 30, 10, 30]
    print(mcm(arr))
    print(mem_memoisation(arr))