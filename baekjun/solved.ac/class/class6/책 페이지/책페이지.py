import sys

def solve(N):
    answer = [0] * 10
    point = 1

    while N != 0:
        while N % 10 != 9:
            for i in str(N):
                answer[int(i)] += point
            N -= 1

        if N < 10:
            for i in range(N + 1):
                answer[i] += point
            answer[0] -= point
            return answer

        for i in range(10):
            answer[i] += (N // 10 + 1) * point
        answer[0] -= point
        point *= 10
        N //= 10

N = int(sys.stdin.readline())
print(*solve(N))