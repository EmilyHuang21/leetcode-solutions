class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        
        candies = [1] * n  # 步驟 1：每個小孩至少拿 1 顆糖果
        
        # 步驟 2：從左到右遍歷，確保右邊的孩子拿更多糖果（如果評分較高）
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # 步驟 3：從右到左遍歷，確保左邊的孩子拿更多糖果（如果評分較高）
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)  # 步驟 4：計算糖果總數