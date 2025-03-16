class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1  # 初始化左右指針
        max_area = 0  # 紀錄最大面積
        
        while left < right:
            # 計算當前容器的面積
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)  # 更新最大面積

            # 移動較矮的指針
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area  # 回傳最大面積