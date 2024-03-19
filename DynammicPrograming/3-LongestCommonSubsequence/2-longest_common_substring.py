def longest_common_substring(s1, s2):
    def longest_common_substring_util(n1, n2, count=0):
        if n1 == 0 or n2 == 0:
            return count
        if s1[n1 -1] == s2[n2 - 1]:
            count = longest_common_substring_util(n1- 1, n2 - 1, count + 1)
        else:
            count = max(count, 
                        max(longest_common_substring_util(n1 - 1, n2, 0), 
                            longest_common_substring_util(n1, n2 - 1, 0)))
        return count
    return longest_common_substring_util(len(s1), len(s2))

def longest_common_substring_memoisation(s1, s2):
    dp = [
        [-1 for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]
    def longest_common_substring_util(n1, n2, count=0):
        if n1 == 0 or n2 == 0:
            return count
        if dp[n1][n2] != -1:
            return dp[n1][n2]
        if s1[n1 - 1] == s2[n2 - 1]:
            dp[n1][n2] = longest_common_substring_util(n1 - 1, n2 - 1, count + 1)
        else:
            dp[n1][n2] = max(count, 
                             max(longest_common_substring_util(n1 - 1, n2, 0), 
                                 longest_common_substring_util(n1, n2 - 1, 0)))
        return dp[n1][n2]
    return longest_common_substring_util(len(s1), len(s2))

def longest_common_substring_topdown(s1, s2):
    dp = [
        [-1 for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]
    result = 0
    for n1 in range(len(s1) + 1):
        for n2 in range(len(s2) + 1):
            if n1 == 0 or n2 == 0:
                dp[n1][n2] = 0
            elif s1[n1 - 1] == s2[n2 - 1]:
                dp[n1][n2] = 1 + dp[n1- 1][n2 - 1]
            else:
                dp[n1][n2] = 0
            result = max(result, dp[n1][n2])
    return result



if __name__ == "__main__":
    txt = "abcdxyz"
    pat = "xyzabcd"
    print(longest_common_substring(txt, pat)) # 4
    print(longest_common_substring_memoisation(txt, pat)) # 4
    print(longest_common_substring_topdown(txt, pat)) # 4