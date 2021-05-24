import sys

def find(index, cnt):
    if cnt == M:
        print(*tmp)
        return

    for i in range(index, len(arr)):
        tmp.append(arr[i])
        find(i, cnt + 1)
        tmp.pop()

N, M = map(int, sys.stdin.readline().split())
arr = sorted(set(list(map(int,sys.stdin.readline().split()))))

dic = {}
tmp = []
find(0, 0)