class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= (n - 1)  # Removes the rightmost 1-bit
            count += 1
        return count