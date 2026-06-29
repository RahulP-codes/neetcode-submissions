class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def df(i, current_str):
            if i == len(digits):
                res.append(current_str)
                return

            for x in mp[digits[i]]:
                df(i+1, current_str + x)

        df(0, "")

        return res