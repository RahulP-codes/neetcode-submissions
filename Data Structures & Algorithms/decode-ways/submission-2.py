class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)

        dp1, dp2 = 1, 0
        prev = ""
        for c in s:
            if c == '0' and prev == '0':
                return 0
            if c == '0' or prev == '0':
                if int(prev) > 2:
                    return 0
                dp1, dp2 = dp2, dp2
            elif int(prev+c) <= 26:
                print('hi')
                dp1, dp2 = dp1+dp2, dp1
            else:
                dp1, dp2 = dp1, dp1
            
            prev = c

        return dp1