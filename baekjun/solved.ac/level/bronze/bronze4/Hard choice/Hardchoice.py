import sys

a, b, c = map(int, sys.stdin.readline().split())
d, e, f = map(int, sys.stdin.readline().split())
answer = 0

if d > a:
    answer += d-a
if e > b:
    answer += e-b
if f > c:
    answer += f-c

print(answer)