"""
a == longest_common_substring(a, b) => Sequence Patter Matching
"""
def detect_pattern(a, b):
    dp = [
        [-1 for _ in range(len(b) + 1)]
        for _ in range(len(a) + 1)
    ]
    for n1 in range(len(a) + 1):
        for n2 in range(len(b) + 1):
            if n1 ==0 or n2 == 0:
                dp[n1][n2] = 0
            elif a[n1 - 1] == b[n2 - 1]:
                dp[n1][n2] = 1 + dp[n1 - 1][n2 - 1]
            else:
                dp[n1][n2] = max(dp[n1-1][n2], dp[n1][n2 - 1])
    return dp[-1][-1] == len(a)

if __name__ == "__main__":
    a = "AXY"
    b = "ADXCPY"
    print(detect_pattern(a, b)) # True