cur = input()
x = int(ord(cur[0]) - ord('a') + 1)
y = int(cur[1])

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

cnt = 0

for m in move:
    next_x = x + m[0]
    next_y = y + m[1]

    if next_x >= 1 and next_x <=8 and next_y >= 1 and next_y <= 8:
        cnt += 1

print(cnt)