class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)  # 提升查找效率
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字串可以拆分

        # 嘗試從 i = 1 到 n
        for i in range(1, n + 1):
            for j in range(i):
                # 檢查 s[j:i] 是否在字典中，且前段可以成功拆分
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # 提前結束內層迴圈

        return dp[n]