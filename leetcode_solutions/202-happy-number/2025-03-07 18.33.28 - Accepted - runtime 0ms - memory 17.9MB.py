class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow, fast = n, get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))  # Move fast pointer twice

        return fast == 1