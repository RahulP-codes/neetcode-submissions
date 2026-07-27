class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        stack = []
        res = []

        def df(i):
            if i == n:
                res.append(stack[:])
                return
            
            df(i+1)

            stack.append(nums[i])
            df(i+1)
            stack.pop()

        df(0)

        return res