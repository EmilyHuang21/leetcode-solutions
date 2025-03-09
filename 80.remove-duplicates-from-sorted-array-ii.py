#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # 長度 <= 2，直接回傳

        slow = 2  # 從索引 2 開始，因為前兩個元素無條件保留

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:  # 確保不超過 2 次
                nums[slow] = nums[fast]
                slow += 1

        return slow  # 回傳最終有效長度
# @lc code=end
