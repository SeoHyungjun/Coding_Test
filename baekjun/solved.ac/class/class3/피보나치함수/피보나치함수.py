import sys


t = int(sys.stdin.readline())

dic = {0:[1, 0], 1:[0, 1]}

def fibo(n):
    if n not in dic:
        if n-1 not in dic:
            fibo(n-1)
        if n-2 not in dic:
            fibo(n-2)
        dic[n] = [dic[n-1][0]+dic[n-2][0], dic[n-1][1]+dic[n-2][1]]


for _ in range(t):
    n = int(sys.stdin.readline())

    if n not in dic:
        fibo(n)

    print(str(dic[n][0]) + ' ' +  str(dic[n][1]))
