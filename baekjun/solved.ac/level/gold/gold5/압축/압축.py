import sys

def solve(stack):
    tmp = 0

    while stack:
        top = stack.pop()

        if top == ')':
            tmp += solve(stack)
        elif top == '(':
            tmp = tmp * int(stack.pop())
            return tmp
        else:
            tmp += 1

    return tmp

S = sys.stdin.readline().rstrip()
stack = list(S)
answer = solve(stack)
print(answer)