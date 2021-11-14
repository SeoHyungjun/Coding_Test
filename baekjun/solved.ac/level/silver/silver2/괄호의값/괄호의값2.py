import sys
dic = {'[':3, '(':2, ')':'(', ']':'['}

arr = list(sys.stdin.readline().rstrip())
stack = []
answer = 0

for i in arr:
    if i == '(' or i == '[':
        stack.append(i)

    elif i == ')' or i == ']':
        first = True
        start = 1
        while stack and stack[-1].isdigit():
            if first:
                start *= int(stack.pop())
                first = False
            else:
                start += int(stack.pop())
        if stack and stack[-1] == dic[i]:
            stack.append(str(start * dic[stack.pop()]))
        else:
            stack.append('F')

for i in stack:
    if i.isdigit():
        answer += int(i)
    else:
        answer = 0
        break
print(answer)