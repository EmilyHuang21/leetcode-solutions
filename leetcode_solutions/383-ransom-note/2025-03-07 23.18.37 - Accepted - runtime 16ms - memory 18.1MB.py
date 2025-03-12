from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count character frequencies in both strings
        ransomCount=Counter(ransomNote)
        magazineCount=Counter(magazine)

        # Check if magazine has enough of each character
        for char,count in ransomCount.items():
            if magazineCount[char] < count:
                return False
        return True


        