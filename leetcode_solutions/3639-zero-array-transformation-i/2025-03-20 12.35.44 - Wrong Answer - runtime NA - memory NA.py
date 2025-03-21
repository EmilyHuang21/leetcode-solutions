class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array

        # Apply difference array updates based on queries
        for li, ri in queries:
            diff[li] -= 1
            diff[ri + 1] += 1

        # Compute the prefix sum of decrements
        decrements = [0] * n
        current_decrement = 0
        for i in range(n):
            current_decrement += diff[i]
            decrements[i] = current_decrement

        # Check if we can zero out nums with the available decrements
        for i in range(n):
            if nums[i] + decrements[i] != 0:
                return False

        return True
