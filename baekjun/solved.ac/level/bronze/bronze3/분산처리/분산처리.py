import sys

T = int(sys.stdin.readline())

answer = []
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    b = b % 4 if b % 4 != 0 else 4
    print(10 if a**b%10 == 0 else a**b%10)