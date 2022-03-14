import sys

def change_arr(arr):
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(arr[i+1] - arr[i])

    return new_arr

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split(',')))

for _ in range(K):
    arr = change_arr(arr)

print(*arr, sep=',')