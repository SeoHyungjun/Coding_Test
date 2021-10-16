import sys
from collections import deque
Dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find_destination_distance(_passenger_x, _passenger_y):
    global g_passenger, g_board
    _destination_x, _destination_y = g_passenger[g_board[_passenger_x][_passenger_y]]

    queue = deque()
    queue.append((_passenger_x, _passenger_y, 0))
    visited = set()
    visited.add((_passenger_x, _passenger_y))

    while queue:
        _cur_x, _cur_y, _use_fuel = queue.popleft()

        if _cur_x == _destination_x and _cur_y == _destination_y:
            return _use_fuel

        for _dx, _dy in Dir:
            _next_x, _next_y = _cur_x + _dx, _cur_y + _dy

            if 0 <= _next_x < N and 0 <= _next_y < N and (_next_x, _next_y)\
                    not in visited and g_board[_next_x][_next_y] != 1:
                queue.append((_next_x, _next_y, _use_fuel + 1))
                visited.add((_next_x, _next_y))

    return -1


def find_nearest_passenger(x, y):
    global g_board, g_passenger

    queue = deque()
    queue.append((x, y, 0))
    visited = set()
    visited.add((x, y))

    nearest_passenger = []

    while queue:
        _cur_x, _cur_y, _use_fuel = queue.popleft()

        if nearest_passenger and nearest_passenger[-1][2] < _use_fuel:
            break

        if g_board[_cur_x][_cur_y] > 1:
            nearest_passenger.append((_cur_x, _cur_y, _use_fuel))
            continue

        for _dx, _dy in Dir:
            _next_x, _next_y = _cur_x + _dx, _cur_y + _dy

            if 0 <= _next_x < N and 0 <= _next_y < N and \
                    (_next_x, _next_y) not in visited and g_board[_next_x][_next_y] != 1:
                queue.append((_next_x, _next_y, _use_fuel + 1))
                visited.add((_next_x, _next_y))

    nearest_passenger.sort(key=lambda _x: (_x[0], _x[1]))
    if nearest_passenger:
        return nearest_passenger[0]
    else:
        return -1, -1, -1


def work_taxi():
    global g_board, g_cur_x, g_cur_y, g_passenger, g_fuel

    _cur_fuel = g_fuel

    while g_passenger:
        _passenger_x, _passenger_y, _distance = find_nearest_passenger(g_cur_x, g_cur_y)
        if _passenger_x == -1 and _passenger_y == -1 and _distance == -1:
            _cur_fuel = -1
            break

        _use_fuel = find_destination_distance(_passenger_x, _passenger_y)
        if _use_fuel == -1:
            _cur_fuel = -1
            break

        _cur_fuel -= _distance + _use_fuel

        if _cur_fuel < 0:
            _cur_fuel = -1
            break

        g_cur_x, g_cur_y = g_passenger[g_board[_passenger_x][_passenger_y]]
        del g_passenger[g_board[_passenger_x][_passenger_y]]
        g_board[_passenger_x][_passenger_y] = 0

        _cur_fuel += 2 * _use_fuel

    return _cur_fuel


if __name__ == "__main__":
    N, M, g_fuel = map(int, sys.stdin.readline().split())
    g_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    g_cur_x, g_cur_y = map(int, sys.stdin.readline().split())
    g_cur_x -= 1
    g_cur_y -= 1

    g_passenger = {}
    for index_passenger in range(2, M + 2):
        a, b, c, d = map(int, sys.stdin.readline().split())
        g_board[a-1][b-1] = index_passenger
        g_passenger[index_passenger] = [c-1, d-1]

    print(work_taxi())


"""
3 2 2
0 0 0
0 0 0
0 0 0
1 1
1 1 3 1
1 2 3 1

-> -1

3 2 1
0 0 0
0 0 0
0 0 0
1 1
1 1 2 1
1 2 1 1

-> -1

"""