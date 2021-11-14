import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
len_bomb = len(bomb)

stack = []

for ch in string:
    stack.append(ch)
    if ch == bomb[-1] and ''.join(stack[-len_bomb:]) == bomb:
        del stack[-len_bomb:]
        
answer = ''.join(stack)

if answer == '':
    print('FRULA')
else:
    print(answer)