import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    while arr[i]:
        sys.stdout.write(str(i) + '\n')
        arr[i] -= 1
