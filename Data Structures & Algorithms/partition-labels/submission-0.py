class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}
        for i in range(len(s)-1, -1, -1):
            if not s[i] in end:
                end[s[i]] = i

        print(end)

        res = []
        curl = 0 
        cut = 0
        for i in range(len(s)):
            cut = max(cut, end[s[i]])
            curl += 1

            if cut == i:
                res.append(curl)
                curl = 0

        return res