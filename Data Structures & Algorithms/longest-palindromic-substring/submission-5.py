class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#'+ "#".join(s) + '#'
            n = len(t)
            p = [0]*n
            c, r = 0, 0

            for i in range(n):
                p[i] = min(r-i, p[c-(i-c)]) if i < r else 0

                while (i+p[i]+1 < n and i-p[i]-1 >= 0 and t[i-p[i]-1] == t[i+p[i]+1]):
                    p[i] += 1

                if i+p[i] > r:
                    c = i
                    r = i + p[i]

            return p

        p = manacher(s)
        print(p)
        maxlen = 0
        idx = 0
        for i, v in enumerate(p):
            if v>maxlen:
                maxlen = v
                idx = i
        print(maxlen, idx)
        start = (idx - maxlen) // 2

        return s[start: start+maxlen]