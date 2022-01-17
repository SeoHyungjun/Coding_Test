import sys

arr = sorted(list(map(int, sys.stdin.readline().split())))

if arr[2] - arr[1] == arr[1] - arr[0]:
    print(arr[2] + arr[1] - arr[0])
elif arr[2] - arr[1] > arr[1] - arr[0]:
    print(arr[1] + arr[1] - arr[0])
elif arr[2] - arr[1] < arr[1] - arr[0]:
    print(arr[0] + arr[2] - arr[1])