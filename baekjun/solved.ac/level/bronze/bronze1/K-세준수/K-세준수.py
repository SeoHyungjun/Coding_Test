import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

primes = [0]*100001
for i in range(2, N+1):
    if primes[i]:
        continue

    for j in range(i, N+1, i):
        #primes[j] = max(primes[j], i)
        primes[j] = i

answer = 0
for i in range(1, N+1):
    if primes[i] <= K:
        answer += 1

print(answer)