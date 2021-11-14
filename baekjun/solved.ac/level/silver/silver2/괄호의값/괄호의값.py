# 17:40 -> 18:40

import sys
from collections import Counter

string = list(sys.stdin.readline().rstrip())
stack = []
dic = {'(':2, '[':3, ')':'(', ']':'['}
answer = 0
check = Counter(string)
if check['('] == check [')'] and check['['] == check[']']:
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)

        else:
            if not stack:
                answer = 0
                break
            tmp = 0
            end = dic[i]
            while stack and stack[-1].isdigit():
                tmp += int(stack.pop())

            if stack[-1] == end:
                stack.pop()

            if tmp == 0:
                stack.append(str(dic[end]))
            else:
                stack.append(str(dic[end] * tmp))
            if stack[0].isdigit():
                answer += int(stack.pop())

print(answer)