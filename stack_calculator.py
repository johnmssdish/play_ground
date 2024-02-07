
# other solution:


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '+':
                result += sign * operand
                operand = 0
                sign = 1
            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ')':
                result += sign * operand
                operand = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        return result + sign * operand