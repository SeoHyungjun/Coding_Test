import sys

while True:
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    answer = 0
    while not(a == b and b == c and c == d):
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        answer += 1

    print(answer)