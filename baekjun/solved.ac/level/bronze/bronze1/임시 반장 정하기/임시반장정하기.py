import sys
from collections import defaultdict

N = int(sys.stdin.readline())
friend = defaultdict(set)

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for student in range(1, N+1):
    for j in range(5):
        for i in range(N):
            if board[student-1][j] == board[i][j] and student-1 != i:
                friend[student].add(i+1)

near, student = 0, 1
for key in friend.keys():
    if len(friend[key]) > near:
        near = len(friend[key])
        student = key
    elif len(friend[key]) == near:
        student = min(student, key)
    
print(student)