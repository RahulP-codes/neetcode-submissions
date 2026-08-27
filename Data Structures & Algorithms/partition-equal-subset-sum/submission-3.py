class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        n = len(nums)

        memo = [[-1]*(total//2 + 1) for _ in range(n)]
        
        def dfs(curSum, i):
            if curSum > total/2:
                return False
            elif curSum == total/2:
                return True
            if i == n:
                return False
            if memo[i][curSum] != -1:
                return memo[i][curSum]

            if dfs(curSum, i+1) or dfs(curSum + nums[i], i+1):
                memo[i][curSum] = 1
            else:
                memo[i][curSum] = 0

            return True if memo[i][curSum] == 1 else False

        return dfs(0, 0)