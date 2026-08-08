class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = [[-a, 'a', 0], [-b, 'b', 0], [-c, 'c', 0]]

        heapq.heapify(chars)

        res = []
        ban = deque([])

        while chars:
            if chars[0][0] >= 0:
                heapq.heappop(chars)
                continue
                
            print(chars)
            res.append(chars[0][1])
            chars[0][0] += 1
            chars[0][2] += 1


            temp = None
            if chars and chars[0][2] >= 2:
                temp = heapq.heappop(chars)
                temp[2] = 0

            if ban:
                ad = ban.popleft()
                heapq.heappush(chars, ad)

            if temp:
                ban.append(temp)
        
        return "".join(res)