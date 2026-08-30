"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        sorted_inters = sorted(intervals, key=lambda x: x.start)

        for idx in range(1, n):
            if sorted_inters[idx-1].end > sorted_inters[idx].start:
                return False
                
        return True