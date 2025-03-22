class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]         # 可用的硬幣面額
        :type amount: int              # 目標金額
        :rtype: int                    # 回傳最少的硬幣數量，無法湊出則回傳 -1
        """

        # 初始化 dp 陣列，大小為 amount + 1
        # dp[i] 表示「湊出金額 i 所需的最少硬幣數」
        # 一開始除了 dp[0] 為 0，其餘皆設為無限大（表示還沒找到解法）
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 湊出 0 元，不需要任何硬幣

        # 遍歷每一種硬幣面額
        for coin in coins:
            # 嘗試湊出從 coin 到 amount 的所有金額
            for i in range(coin, amount + 1):
                # 狀態轉移公式：
                # dp[i] 可以透過 dp[i - coin] + 1（再加一枚 coin）得到
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # 如果 dp[amount] 沒被更新過，代表無法湊出，回傳 -1
        return dp[amount] if dp[amount] != float('inf') else -1
        