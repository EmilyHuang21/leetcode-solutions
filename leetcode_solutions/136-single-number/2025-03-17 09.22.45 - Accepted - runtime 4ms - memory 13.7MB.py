class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0  # Initialize result with 0
        for num in nums:
            result ^= num  # XOR operation

        return result  # The unique number remains
        