class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m, n = len(word1), len(word2)

        # 建立 DP 表格，大小為 (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化第一列（把 word1 轉換成空字串）
        for i in range(m + 1):
            dp[i][0] = i  # 全部刪除

        # 初始化第一行（把空字串轉換成 word2）
        for j in range(n + 1):
            dp[0][j] = j  # 全部插入

        # 開始填 DP 表格
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 字元相同，不需操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 插入、刪除、替換 三種情況取最小
                    dp[i][j] = min(
                        dp[i - 1][j],     # 刪除
                        dp[i][j - 1],     # 插入
                        dp[i - 1][j - 1]  # 替換
                    ) + 1

        return dp[m][n]
