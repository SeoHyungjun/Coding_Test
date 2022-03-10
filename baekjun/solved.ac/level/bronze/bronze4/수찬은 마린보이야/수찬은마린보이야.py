import sys

N = int(sys.stdin.readline())
if N:
    arr = list(map(float, sys.stdin.readline().split()))

if not N or not sum(arr):
    print("divide by zero")
else:
    print("1.00")