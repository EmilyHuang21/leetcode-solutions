class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indices = {}  # Dictionary to store last seen index of each number

        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True  # Found a duplicate within k distance
            
            num_indices[num] = i  # Update last seen index

        return False  # No valid duplicate found
        