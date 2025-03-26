class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 嘗試在 x 軸 或 y 軸方向做切割
        return self.canCut(rectangles, axis=0) or self.canCut(rectangles, axis=1)

    def canCut(self, rectangles, axis):
        """
        嘗試沿著 x 或 y 軸切割成三個不重疊的區塊
        :param rectangles: 所有矩形資料
        :param axis: 0 = x 軸（垂直切割），1 = y 軸（水平切割）
        """
        # 提取 axis 對應的 start 和 end
        starts = [r[axis] for r in rectangles]
        ends = [r[axis + 2] for r in rectangles]

        # 根據 start 排序，再搭配 end，形成區段
        intervals = sorted(zip(starts, ends))

        groups = []
        curr_group = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_end = curr_group[-1][1]
            cur_start, cur_end = intervals[i]

            if cur_start >= prev_end:
                # 不重疊，可以開始新區塊
                groups.append(curr_group)
                curr_group = [intervals[i]]
            else:
                # 有重疊，合併到當前群組
                curr_group.append(intervals[i])

        groups.append(curr_group)

        # 至少分成 3 區才能有兩條切割線
        return len(groups) >= 3