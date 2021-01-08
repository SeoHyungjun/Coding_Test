# n 세로, m 가로
n, m = map(int, input().split())
# 시작위치 (a, b), 방향(direction) d
a, b, d = map(int, input().split())

# map_arr / 바다 1, 육지 0
map_arr = []
# check / 가본곳 1, 안가본곳 0
check = [[0] * m for _ in range(n)]

for _ in range(n):
    map_arr.append(list(map(int, input().split())))

# 방향 / 북 0, 동 1, 남 2, 서 3
change = [(-1, 0), (0, 1), (1, 0), (0, -1)]

change_cnt = 0
# 첫 위치는 무조건 육지라고 가정
answer = 1

while True:
    # 바라보는 방향을 반시계 방향으로 1번 변경
    # 반시계방향으로 돌면 0 -> 3 -> 2 -> 1
    d -= 1
    change_cnt += 1
    if d == -1:
        d = 3

    next_a = a + change[d][0]
    next_b = b + change[d][1]
    #print(next_a, next_b, change_cnt)

    #if next_a < 0 or next_a > n or next_b < 0 or next_b > m:
    #    print('out')

    #else:
    if next_a >= 0 and next_a < n and next_b >= 0 and next_b < m:
        # 왼쪽 방향에 가보지 않은 칸 존재하고 육지라면
        if check[next_a][next_b] == 0 and map_arr[next_a][next_b] == 0:
            # 위치를 변경하고
            a = next_a
            b = next_b
            # 이동한 위치를 체크
            check[a][b] = 1
            # 방향 전환 횟수 초기화
            change_cnt = 0
            # 이동한 육지 수 증가
            answer += 1
            continue

    # 4방향 모두 확인했으면 
    if change_cnt == 4:
        # 바라보는 반대 방향으로 한칸 이동 but 뒤가 바다일 경우 움직임 멈춤
        next_a = a - change[d][0]
        next_b = b - change[d][1]

        if map_arr[next_a][next_b] == 0:
            a = next_a
            b = next_b
            change_cnt = 0
        else:
            break

print(answer)