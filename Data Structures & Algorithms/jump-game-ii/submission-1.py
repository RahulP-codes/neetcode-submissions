class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return 0

        res = 0
        jump = 0
        curBest = nums[0]

        for i in range(n):
            if i+nums[i] >= n-1:
                return res+1

            if i+nums[i] > curBest:
                curBest = i+nums[i]

            if jump == i:
                res += 1
                jump = curBest

            











                