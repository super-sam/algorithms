def longest_common_subsequence(s1, s2):
    def longest_common_subsequence_util(n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        elif s1[n1 - 1] == s2[n2 - 1]:
            return 1 + longest_common_subsequence_util(n1 - 1, n2 - 1)
        else:
            return max(longest_common_subsequence_util(n1 - 1, n2),
                       longest_common_subsequence_util(n1, n2 - 1))
        
    return longest_common_subsequence_util(len(s1), len(s2))

def longest_common_subsequence_memoisation(s1, s2):
    dp = [
        [-1 for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]
    def longest_common_subsequence_util(n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        elif dp[n1][n2] != -1:
            return dp[n1][n2]
        elif s1[n1 - 1] == s2[n2 - 1]:
            dp[n1][n2] = 1 + longest_common_subsequence_util(n1 - 1, n2 - 1)
        else:
            dp[n1][n2] = max(longest_common_subsequence_util(n1 - 1, n2),
                             longest_common_subsequence_util(n1, n2 - 1))
        return dp[n1][n2]
    return longest_common_subsequence_util(len(s1), len(s2))

def longest_common_subsequence_topdown(s1, s2):
    dp = [
        [-1 for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]
    for n1 in range(len(s1) + 1):
        for n2 in range(len(s2) + 1):
            if n1 == 0 or n2 == 0:
                dp[n1][n2] = 0
            elif s1[n1 - 1] == s2[n2 - 1]:
                dp[n1][n2] = 1 + dp[n1 - 1][n2 - 1]
            else:
                dp[n1][n2] = max(dp[n1 - 1][n2], dp[n1][n2 - 1])
    return dp[len(s1)][len(s2)]

if __name__ == "__main__":
    s1 = "yourocks"
    s2 = "youareawesome"
    print(longest_common_subsequence(s1, s2)) # 5
    print(longest_common_subsequence_memoisation(s1, s2)) # 5
    print(longest_common_subsequence_topdown(s1, s2)) # 5