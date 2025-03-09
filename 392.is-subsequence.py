#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Two pointers

        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move s pointer
                i += 1
            j += 1  # Always move t pointer

        return i == len(s)  # If we matched all chars of s, it's a subsequence

# @lc code=end
