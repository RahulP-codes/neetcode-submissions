class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        stack = []
        res = []

        def backtrack(currentN):
            if currentN == n:
                res.append(stack[:])
                return

            # 1
            stack.append(nums[currentN])
            backtrack(currentN+1)
            stack.pop()

            #2
            backtrack(currentN+1)

        backtrack(0)

        return res
        