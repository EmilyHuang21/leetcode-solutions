class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: 依照起點排序
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                # 沒重疊，直接加進去
                merged.append(interval)
            else:
                # 有重疊，更新區間的結尾
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

        