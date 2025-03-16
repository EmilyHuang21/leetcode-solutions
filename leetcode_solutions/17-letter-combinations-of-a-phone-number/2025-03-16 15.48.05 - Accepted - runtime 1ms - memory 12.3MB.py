class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Phone keypad mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            # Base case: If the current combination is complete
            if index == len(digits):
                result.append("".join(path))
                return

            # Recursive case: Try each letter for the current digit
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                path.append(letter)  # Add letter to path
                backtrack(index + 1, path)  # Move to next digit
                path.pop()  # Remove letter (backtrack)

        # Start backtracking from index 0
        backtrack(0, [])
        return result