class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        memo = {}

        def dfs(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            count = dfs(i+1, j)

            if s[i] == t[j]:
                count += dfs(i+1, j+1)

            memo[(i, j)] = count

            return count

        return dfs(0, 0)
