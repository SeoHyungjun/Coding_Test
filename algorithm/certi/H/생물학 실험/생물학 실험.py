cur_decrease = [False] * 200000
def solve(t):
    N, A, B, answer = int(input()), list(map(int, input().split())), list(map(int, input().split())), 0

    while True:
        is_end = True
        for i in range(N):
            if B[i] - A[i] < B[i-1] + B[(i+1) % N]: continue
            cur_decrease[i] = True
            is_end = False

        if is_end: break
        for i in range(N):
            if not cur_decrease[i]: continue
            diff, near_sum, cur_decrease[i] = B[i] - A[i], B[i-1] + B[(i+1) % N], False
            mul = diff // near_sum
            B[i] -= near_sum * mul
            answer += mul

    print("#%d %d"%(t, answer if A == B else -1))

for t in range(1, int(input()) + 1):
    solve(t)