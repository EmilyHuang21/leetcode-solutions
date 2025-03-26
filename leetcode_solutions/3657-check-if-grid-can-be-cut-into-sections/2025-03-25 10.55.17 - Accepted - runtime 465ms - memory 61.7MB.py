class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        def is_valid(axis):
            # Extract intervals based on axis (0: x, 1: y)
            intervals = [(r[axis], r[axis + 2]) for r in rectangles]
            intervals.sort()

            # Attempt 2 cuts — we move a single cut from left to right
            end1 = intervals[0][1]
            for i in range(1, len(intervals)):
                start, end = intervals[i]
                # if this rect is separate from the previous group
                if start >= end1:
                    # now look for a second group end
                    end2 = end
                    for j in range(i + 1, len(intervals)):
                        s2, e2 = intervals[j]
                        if s2 >= end2:
                            return True
                        end2 = max(end2, e2)
                    return False
                end1 = max(end1, end)
            return False

        # Try cutting on x-axis and y-axis
        return is_valid(0) or is_valid(1)
