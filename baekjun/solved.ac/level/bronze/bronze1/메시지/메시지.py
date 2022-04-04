import sys

group = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    print('Group %d'%(group))

    arr = []
    dic = {}
    for i in range(N):
        cur = sys.stdin.readline().split()
        dic[i] = cur[0]
        arr.append(cur[1:])

    flag = False
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == 'N':
                print("%s was nasty about %s"%(dic[(i-j-1+N)%N], dic[i]))
                flag = True

    if not flag:
        print("Nobody was nasty")

    print()
    group += 1