def print_longest_common_subsequence(s1, s2):
    def print_longest_common_subsequence_util(n1, n2):
        if n1 == 0 or n2 == 0:
            return ""
        elif s1[n1 - 1] == s2[n2 - 1]:
            return print_longest_common_subsequence_util(n1 - 1, n2 - 1) + s1[n1 - 1]
        else:
            if n1 > n2:
                return print_longest_common_subsequence_util(n1 - 1, n2)
            else:
                return print_longest_common_subsequence_util(n1, n2 - 1)
    return print_longest_common_subsequence_util(len(s1), len(s2))

def print_longest_common_subsequence_memoisation(s1, s2):
    dp = [
        [" " for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]
    def print_longest_common_subsequence_util(n1, n2):
        if n1 == 0 or n2 == 0:
            return ""
        elif dp[n1][n2] != " ":
            return dp[n1][n2]
        elif s1[n1 - 1] == s2[n2 - 1]:
            dp[n1][n2] = print_longest_common_subsequence_util(n1 - 1, n2 - 1) + s1[n1-1]
        else:
            if n1 > n2:
                dp[n1][n2] = print_longest_common_subsequence_util(n1 - 1, n2)
            else:
                dp[n1][n2] = print_longest_common_subsequence_util(n1, n2 - 1)
        return dp[n1][n2]
    return print_longest_common_subsequence_util(len(s1), len(s2))

def print_longest_common_subsequence_topdown(s1, s2):
    dp = [
        [" " for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]

    for n1 in range(len(s1) + 1):
        for n2 in range(len(s2) + 1):
            if n1 == 0 or n2 == 0:
                dp[n1][n2] = ""
            elif s1[n1 -1] == s2[n2 - 1]:
                dp[n1][n2] = dp[n1 -1][n2 - 1] + s1[n1 -1]
            elif n1 > n2:
                dp[n1][n2] = dp[n1 - 1][n2]
            else:
                dp[n1][n2] = dp[n1][n2 - 1]

    return dp[len(s1)][len(s2)]

def print_longest_common_subsequence_traverse(s1, s2):
    dp = [
        [-1 for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]
    for n1 in range(len(s1) + 1):
        for n2 in range(len(s2) + 1):
            if n1 == 0 or n2 == 0:
                dp[n1][n2] = 0
            elif s1[n1 - 1] == s2[n2 - 1]:
                dp[n1][n2] = 1 + dp[n1 -1][n2 - 1]
            else:
                dp[n1][n2] = max(dp[n1 - 1][n2], dp[n1][n2 - 1])
    result = []
    n1, n2 = len(s1), len(s2)
    while n1 > 0 and n2 > 0:
        if s1[n1 - 1] == s2[n2 - 1]:
            result.append(s1[n1 - 1])
            n1 -= 1
            n2 -= 1
        elif dp[n1 -1][n2] > dp[n1][n2 - 1]:
            n1 -= 1
        else:
            n2 -= 1

    return "".join(result[::-1])
    

if __name__ == "__main__":
    s1 = "acbcf"
    s2 = "abcdaf"
    print(print_longest_common_subsequence(s1, s2)) # yourocks
    print(print_longest_common_subsequence_memoisation(s1, s2))
    print(print_longest_common_subsequence_topdown(s1, s2)) # yourocks
    print(print_longest_common_subsequence_traverse(s1, s2))
    