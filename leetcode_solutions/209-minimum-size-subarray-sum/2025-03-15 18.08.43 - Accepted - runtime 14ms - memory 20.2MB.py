class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0  # Left pointer of the window
        total = 0  # Current sum of the window
        min_length = float('inf')  # Initialize with a large number
        
        for right in range(len(nums)):
            total += nums[right]  # Expand the window
            
            while total >= target:  # Try to shrink the window
                min_length = min(min_length, right - left + 1)
                total -= nums[left]  # Remove the leftmost element
                left += 1  # Move the left pointer
                
        return min_length if min_length != float('inf') else 0  # If no subarray found, return 0
