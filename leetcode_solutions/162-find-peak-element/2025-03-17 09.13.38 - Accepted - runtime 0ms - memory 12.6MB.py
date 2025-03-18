class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2  # Find middle element
            
            if nums[mid] > nums[mid + 1]:  
                # If mid is greater than right neighbor, move left (peak is in left half or at mid)
                right = mid
            else:
                # If mid is smaller than right neighbor, move right (peak is in right half)
                left = mid + 1  

        return left  # Left and right converge to the peak index
        