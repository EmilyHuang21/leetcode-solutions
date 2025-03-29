class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            # 只要兩邊還相等，就繼續往外擴展
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 回傳目前找到的迴文子字串
            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            # 以 s[i] 為中心（奇數長度）
            odd = expandAroundCenter(i, i)
            # 以 s[i] 和 s[i+1] 為中心（偶數長度）
            even = expandAroundCenter(i, i+1)
            
            # 取較長的那個迴文
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
        