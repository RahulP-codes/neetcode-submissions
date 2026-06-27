class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        memo = {}
        res = []
        stack = []

        def df(i, sum):
            if (sum > target) or (i>=len(nums)):
                return
            elif sum == target:
                res.append(stack[:])
                return

            # 1st case
            stack.append(nums[i])
            df(i, sum+nums[i])
            stack.pop()

            # 2nd case
            df(i+1, sum)

        df(0, 0)

        return res
        