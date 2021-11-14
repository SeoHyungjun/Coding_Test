import sys

L, P = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
correct = L*P
for i in range(5):
    arr[i] -= correct

print(*arr)