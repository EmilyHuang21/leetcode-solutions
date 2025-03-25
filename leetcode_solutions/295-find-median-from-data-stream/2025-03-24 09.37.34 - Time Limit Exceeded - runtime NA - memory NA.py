class MedianFinder(object):

    def __init__(self):
        # 初始化：使用一個 list 來存目前所有數字
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        """
        插入 num 到 self.nums 中，並保持 list 排序
        用簡單的線性搜尋 + insert
        """
        if not self.nums:
            self.nums.append(num)
        else:
            inserted = False
            for i in range(len(self.nums)):
                if num < self.nums[i]:
                    self.nums.insert(i, num)  # 插入到正確的位置
                    inserted = True
                    break
            if not inserted:
                self.nums.append(num)  # 如果比所有數字都大，放到最後面
        

    def findMedian(self):
        """
        :rtype: float
        """
        """
        找目前 list 中的中位數
        """
        n = len(self.nums)
        mid = n // 2
        if n % 2 == 1:
            return float(self.nums[mid])
        else:
            return (self.nums[mid - 1] + self.nums[mid]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()