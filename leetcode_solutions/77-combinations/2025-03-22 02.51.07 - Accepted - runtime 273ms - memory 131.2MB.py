class Solution(object):
    def combine(self, n, k):
        """
        :type n: int   # 整數範圍 [1 ~ n]
        :type k: int   # 組合中每組的長度
        :rtype: List[List[int]]  # 所有合法組合
        """
        res = []

        def backtrack(start, path):
            # 終止條件：長度等於 k，收集這個組合
            if len(path) == k:
                res.append(path[:])
                return

            # 從 start 開始選數字
            for i in range(start, n + 1):
                path.append(i)               # 做選擇
                backtrack(i + 1, path)       # 遞迴（往下找）
                path.pop()                   # 撤銷選擇（回溯）

        backtrack(1, [])
        return res
        