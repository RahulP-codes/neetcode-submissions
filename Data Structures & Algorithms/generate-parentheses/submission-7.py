class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        # stack.append(")")
        # stack.append("()")
        # res.append("".join(stack))
        # stack.pop()

        def df(o, c):
            if o == n:
                res.append("".join(stack+[")"]*(n-c)))
                return

            if c < o:
                stack.append(")")
                df(o, c+1)
                stack.pop()

            stack.append("(")
            df(o+1, c)
            stack.pop()

        df(0, 0)

        return res