class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mp = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        res = []
        stack = []

        def df(i):
            if i == len(digits):
                res.append("".join(stack))
                return

            for x in mp[digits[i]]:
                stack.append(x)
                df(i+1)
                stack.pop()

        if digits:
            df(0)

        return res