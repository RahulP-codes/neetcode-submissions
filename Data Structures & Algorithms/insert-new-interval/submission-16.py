class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        for i in range(len(intervals)-2, -1, -1):
            if newInterval[0] < intervals[i][0]:
                intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
            else:
                break

        ans = [intervals[0]]

        for current in intervals[1:]:
            lastE = ans[-1][1]

            if current[0] <= lastE:
                ans[-1][1] = max(lastE, current[1])
            else:
                ans.append(current)

        return ans


