class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0 # 存儲最終數值
        prev_value = 0 # 記錄前一個數字的數值

        # 從右向左遍歷數字
        for i in range(len(s) - 1, -1, -1):
            current_value = roman_map[s[i]]

            # 若當前數值小於前一個數值，表示需要減去該數值
            if current_value < prev_value:
                total -= current_value
            else:
                total -= current_value
            # 更新前一個數值
            prev_value = current_value

        return total
