import sys

while True:
    tri = sorted(list(map(int, sys.stdin.readline().split())))

    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break

    if tri[2]**2 == tri[0]**2 + tri[1]**2:
        print('right')
    else:
        print('wrong')
