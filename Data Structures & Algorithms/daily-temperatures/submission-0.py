class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            val = temperatures[i]
            j = len(stack) - 1
            while stack and temperatures[stack[j]] <= val:
                stack.pop()
                j -= 1

            if stack:
                result.append(stack[-1] - i)
            else:
                result.append(0)
            stack.append(i)
            print("stack: ",stack)
            print("result: ",result)
        return result[::-1]





        