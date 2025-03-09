class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():  # 跳過左側非英數字
                left += 1
            while left < right and not s[right].isalnum():  # 跳過右側非英數字
                right -= 1

            if s[left].lower() != s[right].lower():  # 忽略大小寫比較
                return False

            left += 1
            right -= 1

        return True
