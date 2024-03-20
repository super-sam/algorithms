def shortest_common_supersequencesequence(s1: str, s2: str) -> int:
    def shortest_common_supersequence_util(n1: int, n2: int) -> int:
        if n1 == 0 or n2 == 0:
            return 0
        if s1[n1 -1] == s2[n2 - 1]:
            return 1 + shortest_common_supersequence_util(n1 - 1, n2 -1)
        else:
            return max(shortest_common_supersequence_util(n1 - 1, n2),
                       shortest_common_supersequence_util(n2, n2 - 1))
    length = shortest_common_supersequence_util(len(s1), len(s2))
    return len(s1) + len(s2) - length

if __name__ == "__main__":
    print(shortest_common_supersequencesequence("geek", "eke"))  # 5
    print(shortest_common_supersequencesequence("aggtab", "gxtxayb"))  # 9
    