class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False  # Handle edge cases

        m, n = len(matrix), len(matrix[0])  # Get matrix dimensions
        left, right = 0, m * n - 1  # Binary search boundaries

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)  # Convert 1D index to 2D coordinates
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False  # Target not found
        