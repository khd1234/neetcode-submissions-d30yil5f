class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        
        result = []
        start, end = intervals[0]
        
        i = 1
        while i < len(intervals):
            if intervals[i][0] > end:
                result.append([start, end])
                start, end = intervals[i]
            if intervals[i][1] > end:
                end = intervals[i][1]
            i += 1
        result.append([start, end])
        
        return result
            
            