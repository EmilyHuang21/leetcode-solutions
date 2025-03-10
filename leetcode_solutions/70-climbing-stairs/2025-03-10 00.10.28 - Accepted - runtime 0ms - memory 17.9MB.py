class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev, curr = 1, 2  # Base cases: f(1) = 1, f(2) = 2

        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr  # Fibonacci logic

        return curr