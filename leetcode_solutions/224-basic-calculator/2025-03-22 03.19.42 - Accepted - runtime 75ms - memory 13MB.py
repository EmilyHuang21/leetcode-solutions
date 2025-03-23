class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        result = 0
        sign = 1  # +1 or -1

        i = 0
        while i < len(s):
            char = s[i]

            if char.isdigit():
                # Read full number (could be multi-digit)
                num = int(char)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                    num = num * 10 + int(s[i])
                result += sign * num
                num = 0

            elif char == '+':
                sign = 1

            elif char == '-':
                sign = -1

            elif char == '(':
                # Push current result and sign
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif char == ')':
                # Pop sign and prev_result from stack
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result

            i += 1

        return result
        