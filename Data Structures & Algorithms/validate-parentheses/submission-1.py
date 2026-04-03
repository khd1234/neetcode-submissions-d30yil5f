class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        for symbol in s:
            if symbol in closeToOpen:
                if len(stack) == 0:
                    return False
                elif stack[-1] == closeToOpen[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)

        if len(stack) == 0:
            return True
        return False
