class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        end_max=0
        count=0
        for st,ed in intervals:
            if ed>end_max:
                count+=1
                end_max=ed
        return count