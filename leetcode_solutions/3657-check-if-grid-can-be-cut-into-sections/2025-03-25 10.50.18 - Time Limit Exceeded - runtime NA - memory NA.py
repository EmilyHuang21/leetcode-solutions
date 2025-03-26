class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def isValid(cuts, axis):
            # axis = 0 for vertical (x), 1 for horizontal (y)
            first, second = cuts
            group1, group2, group3 = [], [], []

            for rect in rectangles:
                start = rect[axis]
                end = rect[axis + 2]

                if end <= first:
                    group1.append(rect)
                elif start >= second:
                    group3.append(rect)
                elif start >= first and end <= second:
                    group2.append(rect)
                else:
                    # Rectangle crosses a cut line
                    return False

            # All three groups must be non-empty
            return all([group1, group2, group3])

        # Try all pairs of horizontal cuts (y-axis)
        y_coords = set()
        for rect in rectangles:
            y_coords.add(rect[1])
            y_coords.add(rect[3])
        y_coords = sorted(list(y_coords))

        for i in range(len(y_coords)):
            for j in range(i + 1, len(y_coords)):
                if isValid((y_coords[i], y_coords[j]), 1):
                    return True

        # Try all pairs of vertical cuts (x-axis)
        x_coords = set()
        for rect in rectangles:
            x_coords.add(rect[0])
            x_coords.add(rect[2])
        x_coords = sorted(list(x_coords))

        for i in range(len(x_coords)):
            for j in range(i + 1, len(x_coords)):
                if isValid((x_coords[i], x_coords[j]), 0):
                    return True

        return False
