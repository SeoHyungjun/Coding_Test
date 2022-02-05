import sys

while True:
    A, B, C, D = map(int, sys.stdin.readline().split())

    if A == 0 and B == 0 and C == 0 and D == 0:
        break

    A, B = min(A, B), max(A, B)
    C, D = min(C, D), max(C, D)

    start, end = 1, 100

    while start <= end:
        mid = (start + end)//2
        a, b = A*mid/100, B*mid/100

        if a <= C and b <= D:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    print("%d%%"%(answer))