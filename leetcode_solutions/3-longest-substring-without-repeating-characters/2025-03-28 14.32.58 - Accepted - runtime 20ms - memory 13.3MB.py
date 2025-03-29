class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # 記錄目前子字串中的字元
        left = 0
        max_len = 0

        for right in range(len(s)):
            # 如果有重複字元，從左邊開始縮小視窗
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # 加入新的字元到集合
            char_set.add(s[right])
            
            # 更新最大長度
            max_len = max(max_len, right - left + 1)

        return max_len