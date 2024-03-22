import sys

def palindrome_partitioning(txt) -> int:
    def is_palindrome(s):
        return s == s[::-1]
    
    def palindrome_partitioning_util(i, j):
        if i >= j:
            return 0
        if is_palindrome(txt[i:j+1]):
            return 0
        temp = sys.maxsize
        for k in range(i, j):
            temp = min(temp, 
                       palindrome_partitioning_util(i, k) + 
                       palindrome_partitioning_util(k+1, j) + 
                       1
                )
        return temp
    return palindrome_partitioning_util(0, len(txt) - 1)

def palindrome_partitioning_memo(txt) -> int:
    def is_palindrome(s):
        return s == s[::-1]
    dp = [
        [-1 for _ in range(len(txt))]
        for _ in range(len(txt))
    ]
    def palindrome_partitioning_util(i, j):
        if i >= j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if is_palindrome(txt[i:j+1]):
            return 0
        temp = sys.maxsize
        for k in range(i, j):
            if dp[i][k] == -1:
                dp[i][k] =  palindrome_partitioning_util(i, k)
            if dp[k+1][j] == -1:
                dp[k+1][j] = palindrome_partitioning_util(k+1, j)
            
            temp = min(temp, 1 +dp[i][k] + dp[k+1][j])
        dp[i][j] = temp
        return dp[i][j]
    
    return palindrome_partitioning_util(0, len(txt) - 1)

if __name__ == "__main__":
    txt = "aaa"
    print(palindrome_partitioning(txt))
    print(palindrome_partitioning_memo(txt))