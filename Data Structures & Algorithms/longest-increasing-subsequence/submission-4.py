class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1]*n for _ in range(n)]

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