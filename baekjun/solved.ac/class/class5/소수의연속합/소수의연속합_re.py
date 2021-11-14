import sys

def solve():
    N = int(sys.stdin.readline())

    if N <= 1:
        print(0)
        return

    check = [False, False] + [True] * (N-1)

    M = int(N**0.5)
    for i in range(2, M+1):
        if check[i]:
            for j in range(2*i, N+1, i):
                check[j] = False

    prime = [i for i in range(2, N+1) if check[i]]

    start, end = 0, 0
    sum = prime[0]
    answer = 0

    while True:
        if sum >= N:
            if sum == N:
                answer += 1
            sum -= prime[start]
            start += 1

        else:
            end += 1
            if end >= len(prime):
                break
            sum += prime[end]

    print(answer)

solve()