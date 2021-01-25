import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse = True)

for i in range(n):
    print(arr[i], end = ' ')