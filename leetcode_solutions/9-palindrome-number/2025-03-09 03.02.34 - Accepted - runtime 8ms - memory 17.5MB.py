class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        '''
        思路
        將 x 轉為字串：str(x)
        反轉字串：str(x)[::-1]
        比對正反讀是否相同：str(x) == str(x)[::-1]
        '''