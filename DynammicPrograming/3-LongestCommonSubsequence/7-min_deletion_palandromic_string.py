def min_delete_for_palondromic_string(s: str) -> int:
    def longest_palondromic_subsequence(txt1: str, txt2: str) -> int:
        dp = [
            [-1 for _ in range(len(txt2) + 1)]
            for _ in range(len(txt1) + 1)
        ]
        for n1 in range(len(txt1) + 1):
            for n2 in range(len(txt2) + 1):
                if n1 == 0 or n2 == 0:
                    dp[n1][n2] = 0
                elif txt1[n1 - 1] == txt2[n2 - 1]:
                    dp[n1][n2] = 1 + dp[n1 - 1][n2 - 1]
                else:
                    dp[n1][n2] = max(dp[n1 -1][n2], dp[n1][n2 - 1])
        return dp[-1][-1]
    txt2 = s[::-1]
    return len(s) - longest_palondromic_subsequence(s, txt2)

if __name__ == "__main__":
    print(min_delete_for_palondromic_string("geeks"))  # 3
    print(min_delete_for_palondromic_string("geek"))  # 2
    print(min_delete_for_palondromic_string("aebcbda"))  # 3