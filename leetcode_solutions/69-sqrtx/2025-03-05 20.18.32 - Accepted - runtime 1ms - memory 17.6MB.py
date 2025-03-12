class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x # 0 和 1 的平方根就是自己
        
        left, right = 1, x // 2 # 限制搜尋範圍
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid  # 完美平方數
            elif square < x:
                left = mid + 1  # 向右搜尋
            else:
                right = mid - 1  # 向左搜尋

        return right  # 迴圈結束時，right 為最接近的整數平方根

        