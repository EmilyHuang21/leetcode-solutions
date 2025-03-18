class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

            total_sum += num

        # If max_sum < 0, all numbers are negative, return max_sum
        if max_sum < 0:
            return max_sum

        # Return the maximum of normal and circular subarray sums
        return max(max_sum, total_sum - min_sum)
        