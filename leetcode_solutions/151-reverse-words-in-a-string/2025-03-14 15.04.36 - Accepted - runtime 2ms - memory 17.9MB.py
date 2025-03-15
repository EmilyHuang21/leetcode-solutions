class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim spaces and split words
        words = s.strip().split()

        # Step 2: Reverse the words
        reversed_words = words[::-1]

        # Step 3: Join words with a single space
        return " ".join(reversed_words)