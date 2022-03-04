import sys

cnt = 0
while True:
    cnt += 1
    O, W = map(int, sys.stdin.readline().split())
    if O == 0 and W == 0:
        break

    die = False
    while True:
        com = sys.stdin.readline().split()
        if com[0] == '#' and com[1] == '0':
            break

        if die:
            continue
        
        if com[0] == 'E':
            W -= int(com[1])
        else:
            W += int(com[1])

        if W <= 0:
            die = True

    if die:
        print(cnt, 'RIP')
    elif 0.5*O < W < 2*O:
        print(cnt, ':-)')
    else:
        print(cnt, ':-(')