import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 'A'
if N == 2 and arr[0] == arr[1]:
    answer = arr[0]
elif N > 2:
    a = 0 if arr[0] - arr[1] == 0 else (arr[1] - arr[2]) // (arr[0] - arr[1])
    b = arr[1] - arr[0] * a
    answer = a * arr[-1] + b if [a * arr[i] + b for i in range(N-1)] == arr[1:] else 'B'

print(answer)