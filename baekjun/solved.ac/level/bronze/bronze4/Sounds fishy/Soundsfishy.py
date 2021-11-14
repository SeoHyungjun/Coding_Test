import sys

arr = [int(sys.stdin.readline()) for _ in range(4)]

if arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3]:
    print('Fish Rising')
elif arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3]:
    print('Fish Diving')
elif arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')