import sys

answer = ''
string = '(' + sys.stdin.readline() + ')'
index = 0
stack = []

for index in range(len(string)):
    if 'A' <= string[index] <= 'Z':
        answer += string[index]

    elif string[index] == '(':
        stack.append(string[index])

    elif string[index] == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

    elif string[index] == '*' or string[index] == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(string[index])

    elif string[index] == '+' or string[index] == '-':
        while stack and stack[-1] != '(':
            answer +=  stack.pop()
        stack.append(string[index])

print(answer)