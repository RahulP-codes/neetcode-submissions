class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]

        prod1 = 1
        prod2 = 1

        neg = False

        for n in nums:
            prod1 *= n
            maxp = max(prod1, maxp)
            if neg:
                prod2 *= n
                maxp = max(maxp, prod2)
        
            if n == 0:
                prod1 = 1
                prod2 = 1
            elif n < 1:
                neg = True

        return maxp