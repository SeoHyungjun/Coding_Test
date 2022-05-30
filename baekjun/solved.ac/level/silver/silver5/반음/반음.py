import sys

keyboard = ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B']

N = int(sys.stdin.readline())
sheet = [int(sys.stdin.readline()) for _ in range(N)] 

answer = []
for i in [0, 2, 4, 5, 7, 9, 11]:
    avail = True
    cur = i

    for next in sheet:
        cur += next

        while not (0 <= cur < 12):
            if cur < 0:
                cur += 12
            else:
                cur %= 12

        if keyboard[cur] == '':
            avail = False
            break

    if avail:
        answer.append((keyboard[i], keyboard[cur]))

answer.sort()
for ans in answer:
    print(*ans)