class Solution(object):
    def checkValidCuts(self, n, rectangles):
        def tryCuts(rectangles, axis):
            # Collect (start, end) intervals for the chosen axis
            intervals = [(rect[axis], rect[axis + 2]) for rect in rectangles]
            intervals.sort()

            # Build prefix sum of rectangles ending before or at a point
            endpoints = sorted(set([p for i in intervals for p in i]))
            prefix = [0] * len(endpoints)
            pos = {v: i for i, v in enumerate(endpoints)}

            for start, end in intervals:
                prefix[pos[start]] += 1
                prefix[pos[end]] -= 1

            for i in range(1, len(prefix)):
                prefix[i] += prefix[i - 1]

            # Now try all combinations of two cut points
            for i in range(1, len(endpoints) - 1):
                for j in range(i + 1, len(endpoints)):
                    c1, c2 = endpoints[i], endpoints[j]
                    group1 = group2 = group3 = 0
                    for start, end in intervals:
                        if end <= c1:
                            group1 += 1
                        elif start >= c2:
                            group3 += 1
                        elif start >= c1 and end <= c2:
                            group2 += 1
                        else:
                            break  # Invalid cut
                    else:
                        if group1 > 0 and group2 > 0 and group3 > 0:
                            return True
            return False

        return tryCuts(rectangles, 0) or tryCuts(rectangles, 1)
