import sys

A = int(sys.stdin.readline())
Operation = sys.stdin.readline().rstrip()
B = int(sys.stdin.readline())

if Operation == '*':
    print(A*B)
else:
    print(A+B)