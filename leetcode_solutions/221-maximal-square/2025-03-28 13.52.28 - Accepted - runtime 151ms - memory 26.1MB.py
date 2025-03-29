class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # 建立 DP 陣列並初始化
        dp = [[0] * n for _ in range(m)]
        max_len = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # 第一列或第一行只能自己是 1 才有邊長 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 從左、上、左上 找出最小的，+1
                        dp[i][j] = min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        ) + 1
                    # 更新目前最大邊長
                    max_len = max(max_len, dp[i][j])

        return max_len * max_len  # 回傳面積（邊長²）
        