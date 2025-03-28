class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        if n == 0:
            return 0

        # Step 1: 建立左右最大高度的陣列
        left_max = [0] * n
        right_max = [0] * n

        # 計算每個位置左邊的最大高度
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        # 計算每個位置右邊的最大高度
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        # Step 2: 累加每個位置可以裝的水
        water = 0
        for i in range(n):
            trapped = min(left_max[i], right_max[i]) - height[i]
            if trapped > 0:
                water += trapped

        return water
