import sys

n = int(sys.stdin.readline())

#table = sorted([list(map(int, sys.stdin.readline().split()))  for i in range(n)], key = lambda x : (x[0], x[1]))
table = []
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

table = sorted(table, key = lambda x : (x[1], x[0]))

cur = 0
count = 0
for st, en in table:
    if st >= cur:
        cur = en
        count += 1

print(count)

