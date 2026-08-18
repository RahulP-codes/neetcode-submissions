class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n: True}

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if s[i: i+len(w)] == w:
                    if dp[i+len(w)]:
                        dp[i] = True
                        break

            if i in dp and dp[i] == True:
                continue
            dp[i] = False

        return dp[0]