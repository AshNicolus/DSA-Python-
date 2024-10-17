
class Solution:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return -1

    def is_empty(self) -> bool:
        return len(self.stack) == 0  # Fixing the comparison

    def isValid(self, s: str) -> bool:
        stack = []
        for it in s:
            if it == '(' or it == '[' or it == '{':
                stack.append(it)  # Fixing the push operation
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop() 
                if (it == ')' and ch != '(') or (it == ']' and ch != '[') or (it == '}' and ch != '{'):
                    return False
        
        return len(stack) == 0  
