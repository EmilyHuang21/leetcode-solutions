class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        for li, ri in queries:
            # Apply the query by decrementing each element in the range
            for i in range(li, ri + 1):
                nums[i] -= 1
        
        # Check if all elements are zero
        return all(x == 0 for x in nums)

        