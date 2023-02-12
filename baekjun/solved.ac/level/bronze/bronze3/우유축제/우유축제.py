import sys

N = int(sys.stdin.readline())
milk = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(N):
    if milk[i] == answer % 3: answer += 1

print(answer)