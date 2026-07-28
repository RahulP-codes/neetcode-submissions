class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(st):
            l, r = 0, len(st)-1
            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)

        res = []
        stack = []

        def df(i, st):
            if i == n:
                if st == "":
                    res.append(stack[:])
                return

            news = st+s[i]

            df(i+1, news)
            
            if isPal(news):
                stack.append(news)
                df(i+1, "")
                stack.pop()

        df(0, "")

        return res