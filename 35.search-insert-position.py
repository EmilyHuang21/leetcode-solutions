#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2  # 計算中間索引
            if nums[mid] == target:
                return mid  # 找到目標值，直接回傳索引
            elif nums[mid] < target:
                left = mid + 1  # 移動左邊界
            else:
                right = mid - 1  # 移動右邊界

        return left  # 當 left > right 時，left 就是插入位置
# @lc code=end
