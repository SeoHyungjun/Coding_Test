import sys

def find(cnt):
    if cnt == M:
        print(*tmp)
        return

    for i in range(len(arr)):
        tmp.append(arr[i])
        del arr[i]
        find(cnt+1)
        arr.insert(i, tmp.pop())

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
tmp = []

find(0)