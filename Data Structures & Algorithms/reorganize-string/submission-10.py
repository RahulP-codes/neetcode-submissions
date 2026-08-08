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
        ban = [0, 0]

        i = 0
        while chars:
            res.append(chars[0][1])

            temp = chars[0]
            heapq.heappop(chars)

            if ban[0] < 0:
                heapq.heappush(chars, ban)

            temp[0] += 1
            ban = temp

        return "".join(res)