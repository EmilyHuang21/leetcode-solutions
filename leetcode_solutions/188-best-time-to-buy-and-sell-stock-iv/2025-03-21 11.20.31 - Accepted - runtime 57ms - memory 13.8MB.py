class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        # 特殊情況：等價於無限次交易（Greedy 解）
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[t][d]: 第 d 天，最多交易 t 次的最大利潤
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            maxDiff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + maxDiff)
                maxDiff = max(maxDiff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]