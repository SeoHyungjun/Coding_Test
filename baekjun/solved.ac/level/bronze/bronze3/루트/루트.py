import sys

while True:
    B, N = map(int, sys.stdin.readline().split())

    if B == 0 and N == 0:
        break

    a = int(pow(B, (1/N)))
    b = a+1

    if abs(B - pow(a, N)) <= abs(B - pow(b, N)):
        print(a)
    else:
        print(b)