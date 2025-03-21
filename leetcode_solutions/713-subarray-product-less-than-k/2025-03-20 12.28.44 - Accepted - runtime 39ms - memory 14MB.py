class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0  # 如果 k ≤ 1，則不可能有符合條件的子陣列
        
        product = 1  # 當前窗口內的乘積
        left = 0  # 左邊界
        count = 0  # 計算總共符合條件的子陣列數量

        for right in range(len(nums)):
            product *= nums[right]

            # 當乘積 >= k 時，縮小窗口
            while product >= k:
                product //= nums[left]
                left += 1

            # 計算以 right 結尾的所有子陣列數量
            count += right - left + 1

        return count
        