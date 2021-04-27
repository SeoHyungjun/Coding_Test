import sys

N = int(sys.stdin.readline())

arr = [0]

for _ in range(N):
    com, val = map(int, sys.stdin.readline().split())

    if com == 0:
        arr.append(val)

    else:
        for i in range(len(arr)):
            arr[i] ^= val

arr.sort()
for i in arr:
    print(i, end = ' ')
"""
5
0 4
0 2
1 4
0 5
1 8
"""