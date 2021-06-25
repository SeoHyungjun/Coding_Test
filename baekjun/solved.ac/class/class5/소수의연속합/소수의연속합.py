import sys

def solve():
    N = int(sys.stdin.readline())

    check = [False, False] + [True] * (N-1)

    M = int(N**0.5)
    for i in range(2, M+1):
        if check[i]:
            for j in range(2*i, N+1, i):
                check[j] = False

    prime = [i for i in range(2, N+1) if check[i]]

    start, end = -1, -1
    sum = 0
    answer = 0

    while True:
        if sum >= N:
            if sum == N:
                answer += 1
            start += 1
            sum -= prime[start]

        else:
            end += 1
            if end >= len(prime):
                break
            sum += prime[end]

    print(answer)

solve()