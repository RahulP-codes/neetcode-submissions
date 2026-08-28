class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0] = 0
        for num in range(1, n+1):
            s = 1
            while s ** 2 <= num:
                dp[num] = min(dp[num], 1 + dp[num-s**2])
                s += 1

        return dp[n]