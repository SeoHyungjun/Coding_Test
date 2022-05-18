import sys

E, S, M = map(int, sys.stdin.readline().split())

answer = 1
while True:
    if (answer - E) % 15 == 0 and (answer - S) % 28 == 0 and (answer - M) % 19 == 0:
        break
    answer += 1

print(answer)