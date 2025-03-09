#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Take the first string as the initial prefix
        prefix = strs[0]

        for string in strs[1:]:  # Iterate over the rest of the strings
            # Reduce the prefix if not a match
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                if not prefix:  # If prefix becomes empty, return ""
                    return ""

        return prefix
# @lc code=end
