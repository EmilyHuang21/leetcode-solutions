class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 如果長度不符合就直接回傳 False
        if len(s1) + len(s2) != len(s3):
            return False

        # 建立 DP 表格：dp[i][j] 表示 s3 的前 i+j 是否由 s1 的前 i 和 s2 的前 j 組成
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True  # 空字串可以互相組成

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                # 檢查從 s1 選字是否能對應 s3
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]

                # 檢查從 s2 選字是否能對應 s3
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]

        return dp[len(s1)][len(s2)]
        