import sys

arr = list(map(int, sys.stdin.readline().split()))

if sum(arr) >= 100:
    print("OK")
else:
    m = min(arr)
    if arr[0] == m:
        print("Soongsil")
    elif arr[1] == m:
        print("Korea")
    else:
        print("Hanyang")