import sys

A, B, C, D = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for person in arr:
    person -= 1
    answer = 0
    if person%(A+B) < A:
        answer += 1
    if person%(C+D) < C:
        answer += 1
    print(answer)