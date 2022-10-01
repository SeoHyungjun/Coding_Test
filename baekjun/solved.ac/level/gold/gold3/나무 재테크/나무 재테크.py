import sys
from collections import deque
direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def solve():
    def spring():
        for i in range(N):
            for j in range(N):
                if not board[i][j]: continue
                deleted_idx = 0
                length = len(board[i][j])
                while deleted_idx < length and board[i][j][deleted_idx] <= energy[i][j]:
                    energy[i][j] -= board[i][j][deleted_idx]
                    board[i][j][deleted_idx] += 1
                    deleted_idx += 1

                for _ in range(deleted_idx, length):
                    die[i][j] += board[i][j].pop()//2

    def summer():
        for i in range(N):
            for j in range(N):
                energy[i][j] += die[i][j]
                die[i][j] = 0

    def fall():
        for i in range(N):
            for j in range(N):
                cnt_add_tree = len([cur for cur in board[i][j] if cur % 5 == 0])
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < N): continue
                    for _ in range(cnt_add_tree):
                        board[ni][nj].appendleft(1)

    def winter():
        for i in range(N):
            for j in range(N):
                energy[i][j] += add_energy[i][j]

    N, M, K = map(int, sys.stdin.readline().split())
    add_energy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    energy = [[5]*N for _ in range(N)]
    board = [[deque() for _ in range(N)] for _ in range(N)]
    die = [[0]*N for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, sys.stdin.readline().split())
        board[x-1][y-1].append(z)

    for _ in range(K):
        spring()
        summer()
        fall()
        winter()

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(board[i][j])

    print(answer)

solve()