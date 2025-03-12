class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')  # 初始化為無窮大
        maxProfit = 0 # 初始化最大利潤為 0

        for price in peices:
            # 更新目前的最低價格（最適合買入的價格）
            minPrice = min(minPrice, price)

            # 計算如果在今天賣出，會得到多少利潤
            profit = price - minPrice

            # 更新最大利潤
            max_profit = max(max_profit, profit)
        return maxProfit

