class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        stack = []
        res = []

        def df(i, summ):
            if i == n:
                return
            if summ == target:
                res.append(stack[:])
                return
            elif summ > target:
                return

            stack.append(nums[i])
            df(i, summ+nums[i])
            stack.pop()

            df(i+1, summ)

        df(0, 0)

        return res



        