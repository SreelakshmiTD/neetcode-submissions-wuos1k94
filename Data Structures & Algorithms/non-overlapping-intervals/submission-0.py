class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1,n):
            start , end = intervals[i]
            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd,end)
                res +=1
        return res

            