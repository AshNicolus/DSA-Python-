def InfixtoPostfix(self, s):
    precedence = {"+":1, "-":1, "*":2, "/":2, "^":3}
    stack = []
    output = []
        
    for char in s:
        if char.isalnum():  
            output.append(char)
        elif char == "(":  
            stack.append(char)
        elif char == ")":  
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()  
        else: 
            while (stack and stack[-1] != "(" and
                    precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                    output.append(stack.pop())
            stack.append(char)

      
    while stack:
        output.append(stack.pop())

    return ''.join(output)
        
