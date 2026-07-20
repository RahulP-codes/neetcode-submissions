class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        prevN = -1

        for n in nums:
            if prevN == n:
                count += 1
            else:
                count -= 1

            if count <= 0:
                prevN = n
                count = 1

        return prevN
            
        
