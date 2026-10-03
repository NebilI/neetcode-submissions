from functools import cmp_to_key

class Solution:

    def interval_compare(self, x, y):
        if x[0] > y[0]:
            return 1
        if x[0] < y[0]:
            return -1
        if x[1] > y[1]:
            return 1
        if x[1] < y[1]:
            return -1
        return 0
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=cmp_to_key(self.interval_compare))

        combined = []
        current_interval = intervals[0]
        for x,y in intervals:
            if current_interval[0] <= x <= current_interval[1]:
                current_interval[1] = max(y,current_interval[1])
            else:
                combined.append([current_interval[0], current_interval[1]])
                current_interval = [x,y]
                
        
        combined.append(current_interval)
        return combined