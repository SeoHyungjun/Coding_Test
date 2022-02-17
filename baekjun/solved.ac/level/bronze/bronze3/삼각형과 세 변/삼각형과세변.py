import sys

while True:
    tri = sorted(list(map(int, sys.stdin.readline().split())))

    if sum(tri) == 0:
        break

    if tri[2] >= tri[0] + tri[1]:
        print('Invalid')
    elif tri[0] == tri[1] and tri[1] == tri[2]:
        print('Equilateral')
    elif tri[0] == tri[1] or tri[1] == tri[2] or tri[2] == tri[0]:
        print('Isosceles')
    else:
        print('Scalene')