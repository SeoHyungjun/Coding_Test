import sys

tour = [sys.stdin.readline().rstrip() for _ in range(36)]
answer = 'Valid'

for i in range(1, 36):
    cur = tour[i]
    before = tour[i-1]

    if ((abs(ord(cur[0]) - ord(before[0])) == 1) and (abs(int(cur[1]) - int(before[1]))) == 2):
        continue
    if ((abs(ord(cur[0]) - ord(before[0])) == 2) and (abs(int(cur[1]) - int(before[1]))) == 1):
        continue

    answer = 'Invalid'
    break

if len(set(tour)) != 36:
    answer = 'Invalid'

if not (((abs(ord(tour[0][0]) - ord(tour[-1][0])) == 1) and (abs(int(tour[0][1]) - int(tour[-1][1]))) == 2) or \
    ((abs(ord(tour[0][0]) - ord(tour[-1][0])) == 2) and (abs(int(tour[0][1]) - int(tour[-1][1]))) == 1)):
    answer = 'Invalid'

print(answer)