class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        summ = 0

        for n in nums:
            if summ < 0:
                summ = 0

            summ += n
            
            max_sum = max(summ, max_sum)

        return max_sum