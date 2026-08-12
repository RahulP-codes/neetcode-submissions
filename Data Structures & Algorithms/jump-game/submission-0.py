class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        r = 0
        i = 0
        while i <= r:
            r = max(r, i+nums[i])

            if r >= n-1:
                return True

            i += 1

        return False