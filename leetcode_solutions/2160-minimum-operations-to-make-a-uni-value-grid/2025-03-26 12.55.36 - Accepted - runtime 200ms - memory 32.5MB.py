class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Step 1: Flatten the grid
        nums = [num for row in grid for num in row]

        # Step 2: Check if all differences are divisible by x
        base = nums[0]
        for num in nums:
            if (num - base) % x != 0:
                return -1  # impossible

        # Step 3: Convert all numbers to step counts
        steps = [(num - base) // x for num in nums]

        # Step 4: Find the median step count
        steps.sort()
        median = steps[len(steps) // 2]

        # Step 5: Sum of distance to median
        return sum(abs(s - median) for s in steps)