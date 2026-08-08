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
            print("chars:", chars)
            i += 1
            print("appending", chars[0][1])
            res.append(chars[0][1])
            chars[0][0] += 1
            temp = chars[0]
            print("removing", chars[0])
            heapq.heappop(chars)

            print("new chars:", chars)
            
            print("checking ban", ban)
            if ban:
                print("adding ban", ban)
                heapq.heappush(chars, ban)
                ban = None
                print("updated ban", ban)

            print("chk chars[0][0]", temp)
            if temp[0] < 0:
                ban = temp
            else:
                ban = None
            print("new ban", ban)


        return "".join(res)