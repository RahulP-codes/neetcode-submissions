class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def df(o, c, s):
            if o == n:
                res.append(s + ")"*(n-c))
                return

            if c < o:
                df(o, c+1, s+")")

            df(o+1, c, s+"(")

        df(0, 0, "")

        return res