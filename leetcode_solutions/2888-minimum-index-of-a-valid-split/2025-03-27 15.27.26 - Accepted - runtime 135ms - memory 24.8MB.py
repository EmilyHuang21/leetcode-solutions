class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        n = len(nums)
        
        # Step 1: Find the dominant element (guaranteed to exist)
        count = Counter(nums)
        for k in count:
            if count[k] * 2 > n:
                dominant = k
                total = count[k]
                break

        # Step 2: Track counts while scanning
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
            # Check dominance in left and right
            if left_count * 2 > (i + 1) and (total - left_count) * 2 > (n - i - 1):
                return i

        return -1
