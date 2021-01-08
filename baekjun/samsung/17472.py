# -*- coding: utf-8 -*- 
N, M = input().split()
N = int(N)
M = int(M)
island = []
board = [[0 for i in range(M)] for j in range(N)]
visit = [[0 for i in range(M)] for j in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for i in range(N):
    tmp = input().split()
    for j in range(M):
        board[i][j] = int(tmp[j])
        
        if(board[i][j] == 1):
            island.append((i, j))

def bfs(i, cnt):
    x = i[0]
    y = i[1]
    #visit[x][y] = 1
    board[x][y] = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if  0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
            board[nx][ny] = cnt
            #visit[nx][ny] = 1
            bfs( (nx, ny), cnt)

def change_num(island):
    cnt = 2
    for i in island:
        if(board[i[0]][i[1]] == 1):
            bfs(i, cnt)
            cnt += 1

    return cnt

a = change_num(island)
#print(a)
bridge = [[0 for i in range(a-2)] for j in range(a-2)]

def connect(cnt):
    for i in island:
        check = 0
        dx = 1
        dy = 1

        while 0 < i[1] + dy < M and board[i[0]][i[1] + dy] == 0 :
            dy += 1
            check += 1

        if 0 < i[1] + dy < M and board[i[0]][i[1] + dy] != 0 and check >= 2:
            bridge[board[i[0]][i[1]] - 2][board[i[0]][i[1] + dy] - 2] = check
            bridge[board[i[0]][i[1] + dy] - 2][board[i[0]][i[1]] - 2] = check
        
        check = 0
        dx = 1
        dy = 1
        while 0 < i[0] + dx < N and board[i[0] + dx][i[1]] == 0 :
            dx += 1
            check += 1

        if 0 < i[0] + dx < N and board[i[0] + dx][i[1]] != 0 and check >= 2:
            bridge[board[i[0]][i[1]] - 2][board[i[0] + dx][i[1]] - 2] = check
            bridge[board[i[0] + dx][i[1]] - 2][board[i[0]][i[1]] - 2] = check
    return

connect(a - 1)

for i in range(N):
    print(board[i])

for i in range(a-2):
    print(bridge[i])

uni = [i for i in range(a - 2)]
dis = []
#print(uni)

def find(x):
    if x == uni[x]:
        return x
    else:
        uni[x] = find(uni[x])
        return uni[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x <= y:
        uni[y] = x
    else:
        uni[x] = y
    '''
    if x <= y:
        for i in range(len(uni)):
            if uni[i] == y:
                uni[i] = x
    else:
        for i in range(len(uni)):
            if uni[i] == x:
                uni[i] = y
    '''

for i in range(a-2):
    for j in range(i):
        if bridge[i][j] != 0:
            dis.append([i, j, bridge[i][j]])

#print(dis)
dis.sort(key = lambda x:x[2])
#print(dis)

def kruscal(dis, a):
    result = 0
    for i in dis:
        #print(i)
        
        x = find(i[0])
        y = find(i[1])

        if x != y:
            union(x, y)
            result += i[2]
            a -= 1
        #print(uni)

    #print('a = ' + str(a))
    if a-3 == 0:
        check = 0
        for i in uni:
            if find(uni[i]) != 0:
                check = 1
        if check == 0:
            return result
        else:
            return -1
    else:
        return -1

#print(uni)
result = kruscal(dis, a)
#print(uni)
print(result)