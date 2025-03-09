#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0  # 慢指針，指向唯一元素最後存放的位置
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:  # 若快指針指向不同的數字
                slow += 1  # 慢指針前進
                nums[slow] = nums[fast]  # 更新唯一元素的位置

        return slow + 1  # 唯一數量為索引 + 1
# @lc code=end
