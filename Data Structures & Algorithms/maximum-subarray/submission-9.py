class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        max_sum = nums[0]
        summ = 0

        for i, n in enumerate(nums):
            if summ <= 0:
                summ = 0

            summ += n
            
            max_sum = max(summ, max_sum)

        return max_sum