import sys

direction = {'R':[1, 0], 'L':[-1, 0], 'B':[0, -1], 'T':[0, 1]}
row = {chr(ord('A') + i):i for i in range(8)}
rev_row = {i:chr(ord('A') + i) for i in range(8)}

king, stone, N = sys.stdin.readline().split()
king = [row[king[0]], int(king[1]) - 1]
stone = [row[stone[0]],int(stone[1]) - 1]

for _ in range(int(N)):
    move = sys.stdin.readline().rstrip()

    add_direction = [0, 0]
    for m in move:
        add_direction[0] += direction[m][0]
        add_direction[1] += direction[m][1]

    next_king = [x + y for x, y in zip(king, add_direction)]
    if next_king == stone:
        next_stone = [x + y for x, y in zip(stone, add_direction)]

        if not (0 <= next_stone[0] < 8 and 0 <= next_stone[1] < 8):
            continue
        stone = next_stone
    else:
        if not (0 <= next_king[0] < 8 and 0 <= next_king[1] < 8):
            continue
    king = next_king

print(rev_row[king[0]] + str(king[1]+1))
print(rev_row[stone[0]] + str(stone[1]+1))