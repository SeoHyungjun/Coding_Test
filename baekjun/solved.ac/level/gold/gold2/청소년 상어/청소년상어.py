import sys
import copy
direction = {0:[-1, 0], 1:[-1, -1], 2:[0, -1], 3:[1, -1], 4:[1, 0], 5:[1, 1], 6:[0, 1], 7:[-1, 1]}

def move_fish():
    global board, shark, eated_fish, fish_where, fish

    for num_fish in range(1, 17):
        if num_fish in eated_fish:
            continue
        
        x, y = fish_where[num_fish]
        for i in range(8):
            next_x, next_y = x + direction[(fish[num_fish]+i) % 8][0], y + direction[(fish[num_fish]+i) % 8][1]
            if not (0 <= next_x < 4 and 0 <= next_y < 4):
                continue

            if next_x == shark[0] and next_y == shark[1]:
                continue

            if board[next_x][next_y] == 0:
                board[x][y] = 0

                board[next_x][next_y] = num_fish
                fish[num_fish] = (fish[num_fish]+i) % 8
                fish_where[num_fish] = [next_x, next_y]
                break

            if 1 <= board[next_x][next_y] <= 16:
                board[x][y] = board[next_x][next_y]
                fish_where[board[x][y]] = [x, y]

                board[next_x][next_y] = num_fish
                fish[num_fish] = (fish[num_fish]+i) % 8
                fish_where[num_fish] = [next_x, next_y]
                break

def move_shark(x, y, cnt_eat, depth):
    global board, shark, eated_fish, fish, fish_where
    tmp_board = copy.deepcopy(board)
    tmp_fishs = copy.deepcopy(fish)
    tmp_fish_where = copy.deepcopy(fish_where)
    prev_shark = shark[:]
    answer = cnt_eat + board[x][y]
    cur_cnt_eat = answer
    tmp_fish = board[x][y]
    board[x][y] = 0
    #print(*board, sep='\n', end='\n\n')
    
    shark = [x, y, fish[tmp_fish]]
    if tmp_fish != 0:
        eated_fish.add(tmp_fish)

    move_fish()
    #print(*board, sep='\n', end='\n\n')

    # 상어가 이동 가능한 위치
    cnt_jump = 1
    while 0 <= x + cnt_jump * direction[shark[2]][0] < 4 and 0 <= y + cnt_jump * direction[shark[2]][1] < 4:
        if 1 <= board[x + cnt_jump * direction[shark[2]][0]][y + cnt_jump * direction[shark[2]][1]] <= 16:
            answer = max(answer, move_shark(x + cnt_jump * direction[shark[2]][0], y + cnt_jump * direction[shark[2]][1], cur_cnt_eat, depth + 1))
        cnt_jump += 1
    
    board[x][y] = tmp_fish
    shark = prev_shark[:]
    if tmp_fish != 0:
        eated_fish.remove(tmp_fish)
    board = tmp_board
    fish = tmp_fishs
    fish_where = tmp_fish_where
    return answer

if __name__ == "__main__":
    board = [[0]*4 for _ in range(4)]
    fish = {}
    fish_where = {}

    for i in range(4):
        arr = list(map(int, sys.stdin.readline().split()))
        for j in range(4):
            fish[arr[2*j]] = arr[2*j + 1] - 1
            fish_where[arr[2*j]] = [i, j]
            board[i][j] = arr[2*j]

    shark = [0, 0, fish[board[0][0]]]
    eated_fish = set()
    print(move_shark(0, 0, 0, 0))