import sys

arr = sorted(list(map(int, sys.stdin.readline().split())))

print(abs((arr[3]+arr[0]) - (arr[2]+arr[1])))