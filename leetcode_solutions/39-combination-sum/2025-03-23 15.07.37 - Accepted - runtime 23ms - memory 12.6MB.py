class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, total):
            # Base case: if total equals target, store the path
            if total == target:
                res.append(path[:])
                return

            # If total exceeds, this path won't work
            if total > target:
                return

            # Try each candidate starting from index `start`
            for i in range(start, len(candidates)):
                num = candidates[i]
                # Choose num, and allow same num again (so pass `i`)
                path.append(num)
                backtrack(i, path, total + num)
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return res