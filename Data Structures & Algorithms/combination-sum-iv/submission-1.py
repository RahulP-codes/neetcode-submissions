class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = [[-1]*(target+1) for _ in range(n)]

        def dfs(i, target):
            if target == 0:
                return 1
            elif target < 0:
                return 0
            if i == n:
                return 0

            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = dfs(i+1, target) + dfs(0, target - nums[i])

            return memo[i][target]

        return dfs(0, target)