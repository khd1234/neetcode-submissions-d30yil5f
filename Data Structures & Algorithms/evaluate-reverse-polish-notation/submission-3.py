class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["4","13","5","/","+"]
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack[-2] += stack[-1]
                stack.pop()
            elif tokens[i] == "-":
                stack[-2] -= stack[-1]
                stack.pop()
            elif tokens[i] == "*":
                stack[-2] *= stack[-1]
                stack.pop()
            elif tokens[i] == "/":
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
            else:
                stack.append(int(tokens[i]))
            print(stack)
        
        return stack[0]

                
                

