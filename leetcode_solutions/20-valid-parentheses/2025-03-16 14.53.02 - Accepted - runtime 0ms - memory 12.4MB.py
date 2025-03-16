class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets
        
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop last opened bracket
                if bracket_map[char] != top_element:  # Check if it matches
                    return False
            else:
                stack.append(char)  # If it's an opening bracket, push it onto the stack
        
        return not stack  # If stack is empty, return True
        