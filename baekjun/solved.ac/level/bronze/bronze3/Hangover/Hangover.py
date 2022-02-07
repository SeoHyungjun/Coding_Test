import sys

while True:
    N = float(sys.stdin.readline())
    if N == 0:
        break

    answer = 0
    sum = 0
    while sum < N:
        sum += 1/(answer+2)
        answer += 1

    print("%d card(s)"%answer)