class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move down

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move left

            if top <= bottom:  # Check if still within bounds
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move up

            if left <= right:  # Check if still within bounds
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move right

        return result