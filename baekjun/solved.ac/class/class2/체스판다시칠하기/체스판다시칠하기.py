color = {0:'B', 1:'W'}
board = []

m, n = map(int, input().split())

for _ in range(m):
    board.append(list(input()))

# 8x8보드이므로 최대 32개를 변경해야하나?
min_changes = 64

# 시작 지점 정하기
for y in range(m - 7):
    for x in range(n - 7):
        start_b = 0
        start_w = 1
        cnt_change_start_b = 0
        cnt_change_start_w = 0

        # 시작지점부터 8x8칸 확인하면서 체크
        for i in range(8):
            for j in range(8):
                # B부터 시작과 W부터 시작으로 체크
                if color[start_b] != board[y+i][x+j]:
                    cnt_change_start_b += 1
                if color[start_w] != board[y+i][x+j]:
                    cnt_change_start_w += 1
                start_b, start_w = start_w, start_b
            start_b, start_w = start_w, start_b
        
        min_changes = min(min_changes, min(cnt_change_start_b, cnt_change_start_w))

print(min_changes)