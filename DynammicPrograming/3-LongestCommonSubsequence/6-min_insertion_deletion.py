"""
heap  --> pea
 \       /
  \     /
    ea
"""

def min_insert_delete(txt1, txt2):
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
    deletion = len(txt1) - dp[len(txt1)][len(txt2)]
    insertion = len(txt2) - dp[-1][-1]
    return (deletion, insertion)

if __name__ == "__main__":
    print(min_insert_delete("heap", "pea"))  # (2, 1)
    print(min_insert_delete("geek", "eke"))  # (2, 1)
    print(min_insert_delete("geeksforgeeks", "geeks"))  # (8, 0)

