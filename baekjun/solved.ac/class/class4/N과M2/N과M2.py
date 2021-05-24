import sys

def find(prev, cnt):
    if cnt == M:
        print(*arr)
        return

    for i in range(prev+1, N+1):
        arr.append(i)
        find(i, cnt + 1)
        arr.pop()

N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N+1)]

arr = []
find(0, 0)
