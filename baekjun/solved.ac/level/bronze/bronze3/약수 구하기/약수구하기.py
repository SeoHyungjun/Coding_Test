import sys

N, K = map(int, sys.stdin.readline().split())

prime_arr = []
for i in range(1, N+1):
    if N % i == 0:
        prime_arr.append(i)

if len(prime_arr) < K:
    print(0)
else:
    print(prime_arr[K-1])