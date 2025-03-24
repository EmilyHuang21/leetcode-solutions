class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        # Step 1: Add all intervals before newInterval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])  # Add the merged interval

        # Step 3: Add the rest of the intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
        