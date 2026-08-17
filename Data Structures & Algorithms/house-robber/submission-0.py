class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp1, dp2, dp3 = nums[1], nums[0], 0
        for i in range(2, n):
            temp = max(dp2, dp3)
            dp1, dp2, dp3 = temp+nums[i], dp1, dp2

        return max(dp1, dp2)