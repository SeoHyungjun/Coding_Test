from collections import deque

open_card = []
answer = float('inf')
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = 4

def find(board, r, c, cnt):
    global open_card, answer
    print(board, cnt, open_card)


    state = True
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                state = False
                break

    if state:
        answer = min(answer, cnt)
        return

    for dx, dy in dir:
        for i in range(1, N+1):
            if 0 <= r + dx*i < N and 0 <= c + dy*i < N and board[r+dx*i][c+dy*i] != 0:
                if not open_card: # opencard가 없을 경우
                    open_card.append((board[r+dx*i][c+dy*i], r+dx*i, c+dy*i))
                    find(board, r+dx*i, c+dy*i, cnt+2)
                    open_card.pop()
                    break
                else: # opencard가 있을경우
                    if not(open_card[0][1] == r+dx*i and open_card[0][2] == c+dy*i): # opencard 랑 다른 위치의 카드일 경우
                        if open_card[0][0] != board[r+dx*i][c+dy*i]: # 현재 위치의 카드랑 다를 경우
                            find(board, r+dx*i, c+dy*i, cnt+1)
                            break
                        else: # 현재 위치의 카드랑 opencard가 같을경우
                            tmp = board[r+dx*i][c+dy*i]
                            open_card_num, open_x, open_y = open_card.pop()
                            board[r+dx*i][c+dy*i] = 0
                            board[open_x][open_y] = 0
                            find(board, r+dx*i, c+dy*i, cnt+2)
                            board[r+dx*i][c+dy*i] = tmp
                            board[open_x][open_y] = tmp
                            open_card.append((open_card_num, open_x, open_y))
                            break

def solution(board, r, c):
    find(board, r, c, 0)
    
    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r, c = 1, 0
board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r, c = 0, 1
print(solution(board, r, c))


