#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # 用來存放數值對應的索引
        for i, num in enumerate(nums):
            complement = target - num  # 計算需要的補數
            if complement in num_map:
                return [num_map[complement], i]  # 找到結果並返回索引
            num_map[num] = i  # 將數值與索引存入字典
# @lc code=end
