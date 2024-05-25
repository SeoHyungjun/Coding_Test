import sys

# baekjoon 9506 bronze1

def checkPerfect(n):
    sum = 0
    arr = []

    for i in range(1, n):
        if n % i != 0: continue
        sum += i
        arr.append(i)

    if sum == n: print(n, '= ' + ' + '.join(str(x) for x in arr))
    else: print(n, 'is NOT perfect.')


while True:
    N = int(sys.stdin.readline())
    if N == -1: break

    checkPerfect(N)