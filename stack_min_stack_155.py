# my solution:
class MinStack:

    def __init__(self):
        self.stack = []
        self.top_value = None
        self.min_stack = []

    def push(self, val: int) -> None:

        if len(self.stack) == 0:
            
            self.min_stack = [val]
        else:

            len_min_stack_old = len(self.min_stack)
            for i in range(len_min_stack_old):
                if self.min_stack[i] < val:
                    self.min_stack = self.min_stack[:i]+[val]+self.min_stack[i:]
                    break

            if len_min_stack_old == len(self.min_stack):
                self.min_stack += [val]
        self.stack.append(val)
        self.top_value = val
    def pop(self) -> None:
        if len(self.stack) <= 1:
            self.top_value = None
            self.stack = []
            self.min_stack = []
        else:
            value_remove = self.stack.pop()
            self.top_value = self.stack[-1]
            value_index = self.min_stack.index(value_remove)
            if value_index == len(self.min_stack) - 1:
                self.min_stack = self.min_stack[:-1]
            elif value_index == 0:
                self.min_stack = self.min_stack[1:]
            else:
                self.min_stack = self.min_stack[:value_index]+self.min_stack[value_index+1:]
 

    def top(self) -> int:
        return self.top_value


    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# # other solution:
# class MinStack:

#     def __init__(self):
#         # Initialize two stacks: one for the main elements and one for the minimum elements.
#         self.stack = []
#         self.min_stack = []

#     def push(self, val: int) -> None:
#         # Push the element onto the main stack.
#         self.stack.append(val)

#         # Update the minimum stack. If it's empty or the new value is smaller, push it onto the min_stack.
#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)

#     def pop(self) -> None:
#         # Pop the top element from the main stack.
#         if self.stack:
#             # If the popped element is the current minimum, also pop it from the min_stack.
#             if self.stack[-1] == self.min_stack[-1]:
#                 self.min_stack.pop()
#             self.stack.pop()

#     def top(self) -> int:
#         # Return the top element of the main stack.
#         if self.stack:
#             return self.stack[-1]

#     def getMin(self) -> int:
#         # Return the top element of the min_stack, which represents the minimum element in the stack.
#         if self.min_stack:
#             return self.min_stack[-1]