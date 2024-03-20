def shortest_common_supersequence_topdown(s1, s2):
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
                dp[n1][n2] = max(dp[n1 - 1][n2], dp[n1][n2- 1])
    
    result = []
    n1, n2 = len(s1), len(s2)
    while n1 > 0 and n2 > 0:
        if s1[n1 - 1] == s2[n2 - 1]:
            result.append(s1[n1 - 1])
            n1 -= 1
            n2 -= 1
        elif dp[n1 -1][n2] > dp[n1][n2 - 1]:
            result.append(s1[n1 - 1])
            n1 -= 1
        else:
            result.append(s2[n2 - 1])
            n2 -= 1
    while n1 > 0:
        result.append(s1[n1 - 1])
        n1 -= 1
    while n2 > 0:
        result.append(s2[n2 - 1])
        n2 -= 1
    return "".join(result[::-1])


if __name__ == "__main__":
    print(shortest_common_supersequence_topdown("geek", "eke"))  # geeke
    print(shortest_common_supersequence_topdown("aggtab", "gxtxayb"))  # aggxtxayb
    print(shortest_common_supersequence_topdown("abac", "cab"))  # aggxtxayb