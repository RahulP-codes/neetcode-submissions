class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False]*n for _ in range(n)]
        idx, length = 0, 1

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > length:
                            length = j-i+1
                            idx = i

        return s[idx: idx+length]

