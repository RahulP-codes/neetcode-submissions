class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        l, r = 0, -1
        count = {}
        maxf = 0
        ans = 1
        while r < n:
            if r >= 0 and r < n:
                maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf - k <= 0:
                ans = max(ans, r-l+1)
                r += 1
                if r < n:
                    count[s[r]] = count.get(s[r], 0) + 1
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

        return ans