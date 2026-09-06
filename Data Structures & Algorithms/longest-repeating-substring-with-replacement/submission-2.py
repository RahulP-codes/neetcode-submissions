class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, -1
        count = {}
        ans = 1
        while r < n:
            maxx = 0
            for value in count.values():
                maxx = max(maxx, value)

            mustreplace = r-l+1 - maxx

            if mustreplace - k <= 0:
                ans = max(ans, r-l+1)
                r += 1
                if r < n:
                    count[s[r]] = count.get(s[r], 0) + 1
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

        return ans