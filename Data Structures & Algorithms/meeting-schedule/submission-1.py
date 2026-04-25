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
        for i in range(n):
            a = intervals[i]
            for j in range(i+1,n):
                b= intervals[j]
                if a.start < b.end and b.start <a.end :
                    return False

        return True
