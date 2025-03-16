class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # Edge case: Empty array
        
        num_set = set(nums)  # Convert list to HashSet for O(1) lookups
        longest_streak = 0
        
        for num in num_set:
            # Only start sequence if num-1 is not in the set
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Check how far the consecutive sequence goes
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update longest streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
        