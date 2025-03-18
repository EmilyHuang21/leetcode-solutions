class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize max_sum to the first element (to handle negative cases)
        max_sum = nums[0]
        current_sum = 0  # Running sum of the current subarray

        for num in nums:
            # If current sum is negative, reset it to zero (start fresh subarray)
            if current_sum < 0:
                current_sum = 0

            # Add the current number to the running sum
            current_sum += num

            # Update max_sum if the new sum is larger
            max_sum = max(max_sum, current_sum)

        return max_sum