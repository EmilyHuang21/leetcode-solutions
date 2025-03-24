class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    # Truncate toward zero
                    result = int(float(a) / b)

                stack.append(result)
            else:
                # It's a number; convert and push
                stack.append(int(token))

        return stack[0]  # Final result
        