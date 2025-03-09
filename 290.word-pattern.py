#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))


'''
分割 s 成 words (s.split())
長度檢查：
pattern 和 words 長度不同，直接回傳 False。
利用 set() 檢查對應關係是否唯一：
set(zip(pattern, words)) 紀錄 (字母, 單詞) 配對數量。
set(pattern) 和 set(words) 確保 一對一映射。

'''

# @lc code=end
