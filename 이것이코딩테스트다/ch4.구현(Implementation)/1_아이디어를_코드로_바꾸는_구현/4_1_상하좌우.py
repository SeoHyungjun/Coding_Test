LRUD = [[0, -1], [0, 1], [-1, 0], [1, 0]]

n = int(input())
move = input().split()

cur = [1, 1]

for m in move:
    if m == 'L':
        d = 0
    elif m == 'R':
        d = 1
    elif m == 'U':
        d = 2
    elif m == 'D':
        d = 3

    next = [x + y for x,y in zip(cur, LRUD[d])]

    if 0 < next[0] and next[0] <= n and 0 < next[1] and next[1] <= n:
        cur = next
    
    print(cur)

print(cur)