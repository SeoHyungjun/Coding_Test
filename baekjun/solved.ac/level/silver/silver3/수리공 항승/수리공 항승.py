import sys

N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 1
st = arr[0]
for cur in arr:
    if st <= cur < st + L:
        continue
    st = cur
    answer += 1

print(answer)