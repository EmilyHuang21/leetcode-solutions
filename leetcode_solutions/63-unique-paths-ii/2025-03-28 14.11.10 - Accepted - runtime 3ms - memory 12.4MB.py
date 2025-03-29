class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)       # 行數
        n = len(obstacleGrid[0])    # 列數
        
        # 如果起點或終點是障礙物，直接回傳 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # 建立 dp 陣列，初始化為 0
        dp = [[0]*n for _ in range(m)]
        
        # 起點設為 1
        dp[0][0] = 1
        
        # 填第一列
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]   # 只要前面沒障礙就繼承值
            else:
                dp[0][j] = 0           # 遇到障礙，後面都會是 0
        
        # 填第一行
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        
        # 填其他格子
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[m-1][n-1]