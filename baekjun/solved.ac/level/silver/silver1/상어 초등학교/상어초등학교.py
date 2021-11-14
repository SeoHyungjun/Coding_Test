import sys
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
add_answer = [0, 1, 10, 100, 1000]

def is_favorite(num_my, num_friend):
    if num_friend in student[num_my]:
        return True
    return False

def cal_satisfy():
    answer = 0

    for i in range(N):
        for j in range(N):
            cnt_favorite = 0
            for dx, dy in direction:
                next_x, next_y = i + dx, j + dy
                if not (0 <= next_x < N and 0 <= next_y < N):
                    continue

                if is_favorite(board[i][j], board[next_x][next_y]):
                    cnt_favorite += 1

            answer += add_answer[cnt_favorite]

    return answer

def sit_student(num_st):
    global board

    position = []

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue

            cnt_favorite = 0
            cnt_empty = 0
            for dx, dy in direction:
                next_x, next_y = i + dx, j + dy
                if not (0 <= next_x < N and 0 <= next_y < N):
                    continue

                if board[next_x][next_y] == 0:
                    cnt_empty += 1
                    continue

                if is_favorite(num_st, board[next_x][next_y]):
                    cnt_favorite += 1
                    
            position.append((i, j, cnt_favorite, cnt_empty))

    position.sort(key=lambda x:(-1*x[2], -1*x[3], x[0], x[1]))
    board[position[0][0]][position[0][1]] = num_st


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [[0]*N for _ in range(N)]

    student = {}
    for _ in range(N*N):
        num_student, a, b, c, d = map(int, sys.stdin.readline().split())
        student[num_student] = (a, b, c, d)
        sit_student(num_student)

    print(cal_satisfy())