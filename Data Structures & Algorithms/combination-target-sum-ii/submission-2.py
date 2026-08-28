class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        candidates.sort()

        res = []
        stack = []
        def dfs(i, curSum):
            if curSum == target:
                res.append(stack[:])
                return
            if curSum > target:
                return
            if i == n:
                return
            
            skip = i+1
            while skip < n and candidates[skip] == candidates[skip-1]:
                skip += 1
            
            dfs(skip, curSum)

            stack.append(candidates[i])
            dfs(i+1, curSum + candidates[i])
            stack.pop()
        
        dfs(0, 0)

        return res