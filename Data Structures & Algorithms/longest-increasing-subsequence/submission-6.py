class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            LIS = dfs(i+1, j)

            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS, 1 + dfs(i+1, i))

            memo[i][j] = LIS

            return LIS

        return dfs(0, -1)