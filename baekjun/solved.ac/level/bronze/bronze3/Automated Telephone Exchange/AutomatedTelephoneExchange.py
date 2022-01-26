import sys

N = int(sys.stdin.readline())

answer = 0
for i in range(100):
    for j in range(100):
        if N - i - j == 0:
            answer += 1

print(answer)