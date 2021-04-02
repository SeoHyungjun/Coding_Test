import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = list(input().rstrip('\n'))
    n = int(input())
    arr = input().rstrip('\n')
    if arr == '[]':
        arr = []
    else:
        arr = deque(arr.lstrip('[').rstrip(']').split(','))

    state = True
    rever = False
    for com in p:
        if com == 'R':
            rever = not rever
        elif com == 'D':
            if not arr:
                print('error')
                state = False
                break
            if rever:
                arr.pop()
            else:
                arr.popleft()

    if rever:
        arr.reverse()
    if state:
        print('[' + ','.join(arr) + ']')