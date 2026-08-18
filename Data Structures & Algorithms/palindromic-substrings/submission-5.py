class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0]*n
            c, r = 0, 0

            for i in range(n):
                p[i] = min(r-i, p[2*c - i]) if i < r else 0

                while (i-p[i]-1 >= 0 and i+p[i]+1 < n and t[i+p[i]+1]==t[i-p[i]-1]):
                    p[i] += 1

                if i + p[i] > r:
                    c = i
                    r = i + p[i]

            return p

        p = manacher(s)
        res = 0
        for v in p:
            res += (v+1)//2

        return res