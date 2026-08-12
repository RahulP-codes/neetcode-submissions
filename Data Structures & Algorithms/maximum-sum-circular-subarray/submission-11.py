class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = nums[0]
        minSum = nums[0]

        curmax = 0
        curmin = 0

        total = 0

        for num in nums:
            curmax = max(curmax+num, num)
            curmin = min(curmin+num, num)

            total += num

            maxSum = max(maxSum, curmax)
            minSum = min(minSum, curmin)

        return max(maxSum, total-minSum) if maxSum > 0 else maxSum