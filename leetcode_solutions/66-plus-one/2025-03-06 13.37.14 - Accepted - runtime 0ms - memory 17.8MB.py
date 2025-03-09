class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 從最後一位開始遍歷
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # 直接返回，因為沒有進位需求
            digits[i] = 0 # 若為 9，則變為 0，並繼續進位

        # 如果所有數字都是 9，則在最前方加上 1
        return [1] + digits
        
