import sys
import math

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
arr_diff = []

for i in range(N-1):
    arr_diff.append(arr[i+1] - arr[i])

answer = arr_diff[0]
for i in range(1, N-1):
    answer = math.gcd(answer, arr_diff[i])

print(answer)