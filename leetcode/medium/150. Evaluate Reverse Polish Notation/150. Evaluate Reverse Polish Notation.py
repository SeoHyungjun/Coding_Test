# Runtime : 70ms ~ 144ms
# faster than 82.41% ~ 16?%

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        check = {'+', '-', '*', '/'}
        
        for cur in tokens:
            if cur not in check:
                stack.append(int(cur))
                continue
                
            B = stack.pop()
            A = stack.pop()
            if cur == '+':
                stack.append(A + B)
            elif cur == '-':
                stack.append(A - B)
            elif cur == '*':
                stack.append(A * B)
            else: #elif cur == '/':
                stack.append(int(A/B))

        return stack[0]