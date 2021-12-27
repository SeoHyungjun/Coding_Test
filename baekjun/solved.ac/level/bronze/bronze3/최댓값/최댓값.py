import sys

answer = [0, 0, 0]
for i in range(1, 10):
    for j, val in enumerate(list(map(int, sys.stdin.readline().split()))):
        if val > answer[0]:
            answer = [val, i, j+1]

print(answer[0])
print(answer[1], answer[2])