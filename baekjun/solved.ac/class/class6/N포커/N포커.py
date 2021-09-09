import sys

def solve():
    answer = 0
    for n in range(53):
        nCk[n][0] = nCk[n][n] = 1
        for k in range(1, n):
            nCk[n][k] = nCk[n][n-k] = (nCk[n-1][k-1] + nCk[n-1][k]) % 10007

    for i in range(4, N+1, 4):
        answer += (1 if (i//4)%2 == 1 else -1) * nCk[13][i//4] * nCk[52-i][N-i] % 10007

    return answer % 10007

N = int(sys.stdin.readline())
nCk = [[0] * 53 for _ in range(53)] 

print(solve())