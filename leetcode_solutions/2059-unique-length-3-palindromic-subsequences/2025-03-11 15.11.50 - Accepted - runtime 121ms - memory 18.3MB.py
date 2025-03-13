class Solution:
    '''
    給定一個字串 s，我們要計算長度為 3 的唯一回文子序列數量。
    回文（Palindrome）：指正著讀和倒著讀相同的字串。例如 "aba"、"bbb"。
    子序列（Subsequence）：可以透過刪除部分字元（但不能改變剩餘字母的順序）獲得的新字串。
    例如，"ace" 是 "abcde" 的子序列。

    解題思路:回文長度固定為 3：
    格式為 "X_Y_X"（第一個和第三個字元相同）。
    只需找到符合條件的 X，並計算其之間的唯一 Y。
    最佳化方式（O(n）時間複雜度）：
        遍歷 s 找到 X（第一和最後出現的位置）。
        統計 X 之間的唯一 Y（中間字母）。
    '''
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}  # 記錄每個字母第一次出現的索引
        last = {}   # 記錄每個字母最後一次出現的索引
        
        # 找出每個字母的第一個和最後一個出現位置
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i  # 不斷更新最後一次出現的索引
        
        count = 0  # 計算符合條件的回文數量
        
        # 遍歷所有字母（a-z）
        for char in first:
            if first[char] < last[char]:  # 確保有足夠的間隔來放中間字母
                # 找出 `X_X` 之間的唯一 `Y`
                unique_middles = set(s[first[char] + 1:last[char]])
                count += len(unique_middles)  # 計算唯一中間字母數量
        
        return count
        