class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n  # Step 1: Initialize output array with 1

        # Step 2: Compute prefix products (Left to Right)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]  # Update prefix for next iteration

        # Step 3: Compute suffix products and multiply with prefix (Right to Left)
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]  # Update suffix for next iteration

        return answer
            