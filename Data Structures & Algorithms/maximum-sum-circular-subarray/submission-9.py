class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = nums[0]
        minSum = nums[0]

        currMax = 0
        currMin = 0

        totalSum = 0

        for n in nums:
            currMax = max(currMax+n, n)
            currMin = min(currMin+n, n)

            totalSum += n

            maxSum = max(currMax, maxSum)
            minSum = min(currMin, minSum)

        return max(maxSum, totalSum-minSum) if maxSum > 0 else maxSum