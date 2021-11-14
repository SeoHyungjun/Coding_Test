import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    name, rank = sys.stdin.readline().split()
    arr.append((name, int(rank)))

arr.sort(key = lambda x : x[1])

print(arr)

for i in range(n):
    print(arr[i][0], end = ' ')