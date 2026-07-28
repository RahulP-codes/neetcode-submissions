class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dups = {}
        sing = list(set(nums))

        n = len(sing)

        for x in nums:
            dups[x] = dups.get(x, 0) + 1

        stack = []
        res = []

        def df(i, dup):
            if i == n:
                res.append(stack[:])
                return

            if dup < dups[sing[i]]:
                stack.append(sing[i])
                df(i, dup+1)
                stack.pop()

            df(i+1, 0)

        df(0, 0)

        return res
        