import sys
direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def move_fireball():
    global fireball, g_max_fireball_index
    graph = [[[] for _ in range(N)] for _ in range(N)]
    check_two_over_fireball_in_same_graph = set()

    # fireball 이동
    for _index_fireball in fireball.keys():
        _r, _c, _m, _s, _d = fireball[_index_fireball]

        next_r = (_r + direction[_d][0] * _s + N) % N
        next_c = (_c + direction[_d][1] * _s + N) % N

        if graph[next_r][next_c] and (next_r, next_c) not in check_two_over_fireball_in_same_graph:
            check_two_over_fireball_in_same_graph.add((next_r, next_c))
        graph[next_r][next_c].append(_index_fireball)

        fireball[_index_fireball] = (next_r, next_c, _m, _s, _d)

    # 여러개의 fireball이 들어있는 칸만 확인
    for _x, _y in check_two_over_fireball_in_same_graph:
        cnt_fireball = len(graph[_x][_y])
        # 각 칸의 fireball을 합해줌
        sum_m = 0
        sum_s = 0
        cnt_odd = 0
        cnt_even = 0
        for _index_fireball in graph[_x][_y]:
            _, _, _m, _s, _d = fireball[_index_fireball]
            del fireball[_index_fireball]
            sum_m += _m
            sum_s += _s
            if _d % 2 == 0:
                cnt_even += 1
            else:
                cnt_odd += 1

        new_m = sum_m // 5
        new_s = sum_s // cnt_fireball

        if new_m == 0:
            continue

        if cnt_odd == 0 or cnt_even == 0:  # 모두 홀수 또는 짝수면 0 2 4 6
            new_direction_set = (0, 2, 4, 6)
        else:
            new_direction_set = (1, 3, 5, 7)

        for new_d in new_direction_set:
            fireball[g_max_fireball_index] = (_x, _y, new_m, new_s, new_d)
            g_max_fireball_index += 1


if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())

    fireball = {}
    for i in range(M):
        r, c, m, s, d = map(int, sys.stdin.readline().split())
        fireball[i] = (r, c, m, s, d)
    g_max_fireball_index = M

    for _ in range(K):
        move_fireball()

    answer = 0
    for index_fireball in fireball.keys():
        answer += fireball[index_fireball][2]

    print(answer)

    """
4 4 2
1 2 13 4 3
1 4 12 3 7
4 1 2 5 7
4 2 6 3 0

-> 25

4 6 4
1 1 5 1 1
3 3 5 1 5
1 3 5 1 3
3 1 5 1 7
2 2 5 1 3
3 2 5 1 2

-> 4

4 9 5
3 2 8 5 2
3 3 19 3 4
3 1 7 1 1
4 4 6 4 0
2 1 6 2 5
4 3 9 4 3
2 2 16 1 2
4 2 17 5 3
3 4 3 5 7

-> 33

"""