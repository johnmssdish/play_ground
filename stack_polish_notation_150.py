class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


    #     # other solution:
    #     stack = []

    #     for token in tokens:
    #         if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
    #             stack.append(int(token))
    #         else:
    #             operand2 = stack.pop()
    #             operand1 = stack.pop()
    #             result = self.perform_operation(operand1, operand2, token)
    #             stack.append(result)

    #     return stack[0]

    # def perform_operation(self, operand1: int, operand2: int, operator: str) -> int:
    #     if operator == '+':
    #         return operand1 + operand2
    #     elif operator == '-':
    #         return operand1 - operand2
    #     elif operator == '*':
    #         return operand1 * operand2
    #     elif operator == '/':
    #         # Division between two integers always truncates toward zero
    #         return int(operand1 / operand2)









        # my solution:
        ope_list = ['+', '-', '*', '/']
        def find_index(a_list):
            # print(f'find_index: {a_list}')
            for i in range(len(a_list)-2):
                # print(f'int(a_list[i]): {int(a_list[i])}')
                # print(f'int(a_list[i+1]): {int(a_list[i+1])}')
                # print(f'int(a_list[i]+2): {a_list[i+2]}')
                if a_list[i] not in ope_list and a_list[i+1] not in ope_list and a_list[i+2] in ope_list:
                    return i
        while '+' in tokens or '-' in tokens or '*' in tokens or '/' in tokens:
            start_index = find_index(tokens)
            if tokens[start_index+2] == '+':
                new_result = int(tokens[start_index]) + int(tokens[start_index+1])
                # new_result = "{:.2f}".format(float(tokens[start_index])) + "{:.2f}".format(float(tokens[start_index+1]))
                # new_result = "{:.2f}".format(new_result)
            elif tokens[start_index+2] == '-':
                new_result = int(tokens[start_index]) - int(tokens[start_index+1])
                # new_result = "{:.2f}".format(float(tokens[start_index])) - "{:.2f}".format(float(tokens[start_index+1]))
                # new_result = "{:.2f}".format(new_result)
            elif tokens[start_index+2] == '*':
                new_result = int(tokens[start_index]) * int(tokens[start_index+1])
                # new_result = "{:.2f}".format(float(tokens[start_index])) * "{:.2f}".format(float(tokens[start_index+1]))
                # new_result = "{:.2f}".format(new_result)
            elif tokens[start_index+2] == '/':
                new_result = int(int(tokens[start_index]) / int(tokens[start_index+1]))
                # if new_result < 0 and new_result > -1:
                #     new_result = 0
                # else:
                #     new_result = floor(new_result)
                
                # new_result = "{:.2f}".format(float(tokens[start_index])) // "{:.2f}".format(float(tokens[start_index+1]))
                # new_result = "{:.2f}".format(new_result)
            if start_index == 0:
                right_list = tokens[3:]
                tokens = [str(new_result)] + right_list
            elif start_index+2 == len(tokens)-1:
                left_list = tokens[:start_index]
                tokens = left_list + [str(new_result)]
            else:
                left_list = tokens[:start_index]
                right_list = right_list = tokens[start_index+3:]
                tokens = left_list + [str(new_result)] + right_list
            # print(f'new token: {tokens}\n')

        return int(tokens[0])