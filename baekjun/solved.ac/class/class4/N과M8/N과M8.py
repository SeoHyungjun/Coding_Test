import sys

def find(index):
    if len(tmp) == M:
        print(*tmp)
        return
    
    for i in range(index, len(arr)):
        tmp.append(arr[i])
        find(i)
        tmp.pop()

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
tmp = []
find(0)