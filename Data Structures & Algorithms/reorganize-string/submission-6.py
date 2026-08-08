class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        
        mp = {}
        for c in s:
            if not c in mp:
                mp[c] = 0
            mp[c] += 1

            if mp[c] > (n+1)//2:
                return ""

        chars = []
        for p in mp:
            chars.append([-mp[p], p])

        heapq.heapify(chars)

        print(chars)

        res = []
        ban = None

        i = 0
        while chars:
            res.append(chars[0][1])
            chars[0][0] += 1
            temp = chars[0]
            heapq.heappop(chars)

            if ban:
                heapq.heappush(chars, ban)
                ban = None

            if temp[0] < 0:
                ban = temp

        return "".join(res)