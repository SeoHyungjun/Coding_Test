N, M = map(int, input().split())

# A가 y축(세로), B가 x축(가로)
A, B, d = map(int, input().split())

map_arr = []
check = [[0 for i in range(N)] for i in range(M)]
print(check)

for i in range(N):
    map_arr.append(list(map(int, input().split())))
print(map_arr)

# 다음 갈곳 위치 정하는것은 현재 바라보는 방향을 기준으로
# 북 0, 동 1, 남 2, 서 3
# 북 -> 서,  동 -> 북, 남 -> 동, 서 -> 남
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

check[A][B] = 1

while True:
    next_A = A + move[d][0]
    next_B = B + move[d][1]

    if map[next_A][next_B] == 1 or check[next_A][next_B] == 1:
        d = (d + 1) % 4
        continue
    #if map[next_A][next_B] == 0 and check[next_A][next_B] == 0:
    else:
        A = next_A
        B = next_B
        d = (d+1) % 4