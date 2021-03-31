import sys
input = sys.stdin.readline
from collections import Counter

answer = [0, 0, 0]

def check_numbers(arr):
    check = [0, 0, 0]
    for i in arr:
        if not check[0] and -1 in i:
            check[0] = 1
        if not check[1] and 0 in i:
            check[1] = 1
        if not check[2] and 1 in i:
            check[2] = 1

        if sum(check) > 1:
            return 4

    if check[0] == 1:
        return -1
    elif check[1] == 1:
        return 0
    elif check[2] == 1:
        return 1

def check_board(arr):
    global answer
    size = len(arr)//3
    state = check_numbers(arr)
    if state == -1:
        answer[0] += 1
    elif state == 0:
        answer[1] += 1
    elif state == 1:
        answer[2] += 1
    else:
        for i in range(3):
            for j in range(3):
                check_board([sub[j*size:(j+1)*size] for sub in arr[i*size:(i+1)*size]])
\

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

check_board(board)

for i in answer:
    print(i)