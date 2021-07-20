import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

start = 0
end = len(arr)-1
tmp = arr[start] + arr[end]
a, b, answer = start, end, arr[start]+arr[end]
while True:
    if tmp < 0:
        start += 1
    elif tmp > 0:
        end -= 1
    else:
        break

    if start >= end:
        break

    tmp = arr[start] + arr[end]
    if abs(tmp) < abs(answer):
        a = start
        b = end
        answer = tmp

print(arr[a], arr[b])