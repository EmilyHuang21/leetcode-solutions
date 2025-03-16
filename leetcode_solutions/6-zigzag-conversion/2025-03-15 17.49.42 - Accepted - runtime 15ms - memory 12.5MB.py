class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):  
            return s  # No need for zigzag if there's only 1 row or string is short

        rows = [""] * numRows  # Create a list to store characters for each row
        index, direction = 0, 1  # Start at row 0 and move downward

        for char in s:
            rows[index] += char  # Append character to the current row
            
            # Change direction at the first or last row
            if index == 0:
                direction = 1  # Move down
            elif index == numRows - 1:
                direction = -1  # Move up
            
            index += direction  # Update row index

        return "".join(rows)  # Join all rows together
        