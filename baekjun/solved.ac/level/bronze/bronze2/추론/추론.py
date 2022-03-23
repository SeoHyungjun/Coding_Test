import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

if arr[1] - arr[0] == arr[2] - arr[1]:
    print(arr[-1] + arr[1] - arr[0])
else:
    print(arr[-1] * (arr[1]//arr[0]))