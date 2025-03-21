class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub):
            return sub == sub[::-1]  # Check if a substring is a palindrome

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:  # Found a mismatch
                # Remove one character and check if the remaining is a palindrome
                return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
            left += 1
            right -= 1

        return True  # If the entire string is already a palindrome