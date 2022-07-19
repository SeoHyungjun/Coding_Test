import sys

direction = [[1, 0], [0, -1], [-1, 0], [0, 1]] # R -> index + 1, L -> index - 1

N = int(sys.stdin.readline())
move = sys.stdin.readline().rstrip()

min_x, min_y, max_x, max_y = 0, 0, 0, 0
d = 0
move_arr = [(0, 0)]
for m in move:
    if m == 'R':
        d = (d + 1) % 4
    elif m == 'L':
        d = (d + 3) % 4
    else:
        x, y = move_arr[-1][0] + direction[d][0], move_arr[-1][1] + direction[d][1]
        min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y)
        move_arr.append((x, y))

answer = [['#'] * (max_y - min_y + 1)  for _ in range(max_x - min_x + 1)]
for x, y in move_arr:
    answer[x - min_x][y - min_y] = '.'

for l in answer:
    print(*l, sep = '')