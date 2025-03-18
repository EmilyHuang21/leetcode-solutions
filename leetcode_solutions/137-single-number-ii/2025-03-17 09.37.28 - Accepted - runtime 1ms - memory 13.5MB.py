class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0  # Initialize bit counters

        for num in nums:
            ones = (ones ^ num) & ~twos  # Appears once
            twos = (twos ^ num) & ~ones  # Appears twice

        return ones  # The single number remains
