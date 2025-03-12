class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res, start = [], 0  # 初始化結果陣列和起始索引

        for i in range(len(nums)):
            # 當數字不連續或到達最後一個數字
            if i + 1 == len(nums) or nums[i] + 1 != nums[i + 1]:
                res.append(str(nums[start]) if start ==
                           i else f"{nums[start]}->{nums[i]}")
                start = i + 1  # 更新新的區間起點

        return res