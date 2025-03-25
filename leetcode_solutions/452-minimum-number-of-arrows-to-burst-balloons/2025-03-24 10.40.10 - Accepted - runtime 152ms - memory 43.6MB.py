class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # Step 1: 依照右邊界排序
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]  # 第一支箭打在第一顆氣球的右邊界

        for start, finish in points[1:]:
            if start > end:
                # 這顆氣球沒被打到，需要再射一箭
                arrows += 1
                end = finish  # 更新新的箭的位置（新的右邊界）

        return arrows

        