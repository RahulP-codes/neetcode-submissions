class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)
        dp = [-1]*(amount+1)
        rcoins = n-1
        for i in range(n):
            if coins[i] == amount:
                return 1
            if coins[i] > amount:
                rcoins = i
                break
            dp[coins[i]] = 1

        for num in range(1, amount+1):
            for i in range(0, rcoins+1):
                coin = coins[i]
                if dp[num] == 1 or coin >= num:
                    break
                if dp[num-coin] != -1:
                    if dp[num] == -1:
                        dp[num] = dp[num-coin] + 1
                    dp[num] = min(dp[num-coin] + 1, dp[num])
                # print(num, coin, dp)

        return dp[amount]
                