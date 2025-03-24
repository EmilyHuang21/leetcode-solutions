class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # Final result list to hold all permutations

        def backtrack(path, used):
            # If the path contains all numbers, it's a valid permutation
            if len(path) == len(nums):
                res.append(path[:])  # Make a copy and store it
                return

            # Try each number in nums
            for i in range(len(nums)):
                if i in used:
                    continue  # Skip if already used in this path

                # Choose the number nums[i]
                used.add(i)
                path.append(nums[i])

                # Continue building the path
                backtrack(path, used)

                # Backtrack: remove the number and mark it unused
                path.pop()
                used.remove(i)

        # Start backtracking with an empty path and empty used set
        backtrack([], set())
        return res
        