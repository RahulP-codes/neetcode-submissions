class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        prevF = intervals[0][0]
        prevE = intervals[0][1]

        ans = []

        for p in intervals:
            if prevE < p[0]:
                ans.append([prevF, prevE])
                prevF = p[0]

            prevE = max(p[1], prevE)

        ans.append([prevF, prevE])

        return ans