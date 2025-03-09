class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) -1, 0

         # 忽略結尾的空格
        while i >= 0 and s[i] == '':
            i -= 1
        
        # 計算最後一個單詞的長度
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length

        