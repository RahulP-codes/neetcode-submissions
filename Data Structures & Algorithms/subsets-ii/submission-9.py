class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        stack = []
        res = []

        def df(i):
            if i == n:
                res.append(stack[:])
                return

            stack.append(nums[i])
            df(i+1)
            stack.pop()

            while i < n-1 and nums[i] == nums[i+1]:
                i += 1

            df(i+1)

        df(0)

        return res
        