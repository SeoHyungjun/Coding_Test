import sys

seq = sys.stdin.readline().rstrip()

where = 0
for s in seq:
    if s == 'A':
        if where == 0:
            where = 1
        elif where == 1:
            where = 0

    elif s == 'B':
        if where == 1:
            where = 2
        elif where == 2:
            where = 1

    else:
        if where == 0:
            where = 2
        elif where == 2:
            where = 0

print(where + 1)