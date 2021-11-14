import sys

def find_max(board):
    # 블럭
    tetro = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]]
    answer = 0
    
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            for te in tetro:
                state = True
                tetro_sum = 0
                for dx, dy in te:
                    if 0 <= i + dx < n and 0 <= j + dy < m:
                        tetro_sum += board[i+dx][j+dy]
                    else:
                        state = False

                if state:
                    answer = max(answer, tetro_sum)

    return answer

N, M = map(int, sys.stdin.readline().split())

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

print(find_max(board))