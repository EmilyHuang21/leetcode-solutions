#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:  # If there is a profit opportunity
                profit += prices[i] - prices[i - 1]  # Buy at i-1, sell at i
        return profit
# @lc code=end
