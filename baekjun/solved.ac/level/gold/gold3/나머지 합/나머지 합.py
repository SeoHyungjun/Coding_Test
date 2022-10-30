import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
mod_value = [0] * M

mod_value[arr[0]%M] += 1
for i in range(1, N):
    arr[i] += arr[i-1]
    mod_value[arr[i] % M] += 1

answer = mod_value[0]
for i in mod_value:
    answer += i * (i-1) // 2 # nC2 = n * (n-1) / 2

print(answer)