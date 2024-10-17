class MinStack:

    def __init__(self):
        self.arr = []  # Stack to store all values
        self.min_stack = []  # Stack to store (minimum_value, count)

    def push(self, val: int) -> None:
        self.arr.append(val)
        # If min_stack is empty or the new value is smaller, push it to min_stack
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append((val, 1))
        elif val == self.min_stack[-1][0]:
            # If the value is equal to the current minimum, increment the count
            self.min_stack[-1] = (val, self.min_stack[-1][1] + 1)

    def pop(self) -> None:
        if not self.is_empty():
            popped_val = self.arr.pop()
            # If the popped value is the same as the current minimum
            if popped_val == self.min_stack[-1][0]:
                if self.min_stack[-1][1] > 1:
                    # If the minimum appears multiple times, decrement the count
                    self.min_stack[-1] = (self.min_stack[-1][0], self.min_stack[-1][1] - 1)
                else:
                    # Otherwise, remove the minimum
                    self.min_stack.pop()
        else:
            return -1

    def top(self) -> int:
        if not self.is_empty():
            return self.arr[-1]
        else:
            return -1

    def is_empty(self) -> bool:
        return len(self.arr) == 0

    def getMin(self) -> int:
        if not self.is_empty():
            return self.min_stack[-1][0]  # Return the current minimum value
        else:
            return -1
