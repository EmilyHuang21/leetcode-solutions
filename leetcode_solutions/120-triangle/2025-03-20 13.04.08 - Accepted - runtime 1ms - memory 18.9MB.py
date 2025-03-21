class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # Start from the second-last row and move upwards
        for i in range(n-2, -1, -1):  
            for j in range(len(triangle[i])):  
                # Update triangle[i][j] with the best path sum
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]  # The top element contains the minimum path sum
