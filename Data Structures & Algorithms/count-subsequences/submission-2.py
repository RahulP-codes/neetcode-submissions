from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def df(sid, tid):
            if (tid >= len(t)):
                return 1
            if (sid >= len(s)):
                return 0

            if (s[sid] == t[tid]):
                return df(sid+1, tid+1) + df(sid+1, tid)
            
            return df(sid+1, tid)

        res = df(0,0)

        return res