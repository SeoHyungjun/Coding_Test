import sys

N, M, K = map(int, sys.stdin.readline().split())

answer = 0
while N >= 2 and M >= 1 and N + M >= K + 3:
    N -= 2
    M -= 1
    answer += 1

print(answer)