# 2021-02-18 20:00 ->  ?????매우 오래걸림... 다음날 추가적으로풀어서 겨우~

import sys

tile = {1:[[0,0]], 2:[[0,0],[0,1]], 3:[[0,0],[1,0]]}
green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]
count = 0

n = int(sys.stdin.readline())

for i in range(n):
    t, x, y = map(int, sys.stdin.readline().split())
    
    where = []
    x_min = 7
    y_min = 7
    green_wh = []
    blue_wh = []
    for a, b in tile[t]:
        where.append([x+a, y+b])
        if x_min > x+a:
            x_min = x+a
        if y_min > y+b:
            y_min = y+b                          

    for a, b in where:
        green_wh.append([a-x_min, b])
        blue_wh.append([a, b-y_min])
    
    # green에서 빈자리 찾아서 이동
    for i in range(6):
        check = 1
        for a, b in green_wh:
            if not (a+1 < 6 and green[a+1][b] == 0):
                check = 0
                break
        
        if check == 1:
            for i in range(len(green_wh)):
                green_wh[i][0] += 1

    for a, b in green_wh:
        green[a][b] = 1

    # blue에서 빈자리 찾아서 이동
    for i in range(6):
        check = 1
        for a, b in blue_wh:
            if not (b+1 < 6 and blue[a][b+1] == 0):
                check = 0
                break
        
        if check == 1:
            for i in range(len(blue_wh)):
                blue_wh[i][1] += 1

    for a, b in blue_wh:
        blue[a][b] = 1


    # green에서 4개 찼을때 제거
    for i in range(2, 6):
        if 0 not in green[i]:
            for j in range(i, 0, -1):
                green[j] = green[j-1]
            green[0] = [0, 0, 0, 0]
            count += 1
        
    for i in range(2):
        if 1 in green[i]:
            for j in range(5, 0, -1):
                green[j] = green[j-1]
            green[0] = [0, 0, 0, 0]

    # blue에서 4개 찼을때 제거
    for i in range(2, 6):
        if blue[0][i] and blue[1][i] and blue[2][i] and blue[3][i]:
            for j in range(i, 0, -1):
                blue[0][j] = blue[0][j-1]
                blue[1][j] = blue[1][j-1]
                blue[2][j] = blue[2][j-1]
                blue[3][j] = blue[3][j-1]
            blue[0][0] = 0
            blue[1][0] = 0
            blue[2][0] = 0
            blue[3][0] = 0
            count += 1
        
    for i in range(2):
        if blue[0][i] or blue[1][i] or blue[2][i] or blue[3][i]:
            for j in range(5, 0, -1):
                blue[0][j] = blue[0][j-1]
                blue[1][j] = blue[1][j-1]
                blue[2][j] = blue[2][j-1]
                blue[3][j] = blue[3][j-1]
            blue[0][0] = 0
            blue[1][0] = 0
            blue[2][0] = 0
            blue[3][0] = 0

print(count)
print( sum([sum(green[i]) for i in range(6)]) + sum([sum(blue[i]) for i in range(4)]) )
