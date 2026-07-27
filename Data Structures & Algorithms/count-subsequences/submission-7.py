class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen = len(s)
        tlen = len(t)

        memo = {}

        def df(i, j):
            if j >= tlen:
                return 1
            if i >= slen:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                memo[(i,j)] = df(i+1, j+1) + df(i+1, j)
                return memo[(i,j)]

            memo[(i, j)] = df(i+1, j)
            return memo[(i, j)] 

        return df(0,0)