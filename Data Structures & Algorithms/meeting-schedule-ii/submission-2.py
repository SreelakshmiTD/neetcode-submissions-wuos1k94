"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda interval:interval.start)
        n = len(intervals)
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        s = e = 0
        rooms = max_rooms = 0
        while s < n:
            if start[s] < end[e]:
                rooms+=1
                max_rooms = max(max_rooms,rooms)
                s +=1
            else:
                rooms -= 1
                e +=1
        return max_rooms
