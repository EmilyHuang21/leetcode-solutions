class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # 初始化狀態
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # 每個狀態都依賴上一狀態更新
            buy1 = max(buy1, -price)            # 最佳第一次買入價
            sell1 = max(sell1, buy1 + price)    # 最佳第一次賣出利潤
            buy2 = max(buy2, sell1 - price)     # 用第一次賺的錢買第二次
            sell2 = max(sell2, buy2 + price)    # 最佳第二次賣出利潤

        return sell2  # 最終最大利潤
        