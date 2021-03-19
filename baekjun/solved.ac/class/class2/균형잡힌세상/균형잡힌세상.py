import sys

while True:
    check = True
    stack = []

    line = sys.stdin.readline().rstrip('\n')
    
    if line == '.':
        break

    for s in line:
        if s == '[':
            stack.append('[')
        elif s == '(':
            stack.append('(')

        elif s == ']':
            if (not stack) or stack.pop() != '[':
                check = False
                break
        elif s == ')':
            if (not stack) or stack.pop() != '(':
                check = False
                break
    
    if check and (not stack):
        print('yes')
    else:
        print('no')

