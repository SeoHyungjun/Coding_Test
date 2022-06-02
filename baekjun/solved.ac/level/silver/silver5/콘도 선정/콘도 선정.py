import sys

N = int(sys.stdin.readline())
condo = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

check = 10001
answer = 0
for D, C in condo:
    if C < check:
        check = C
        answer += 1

print(answer)