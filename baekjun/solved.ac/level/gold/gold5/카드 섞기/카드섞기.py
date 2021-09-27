import sys

def changeArr(arr):
    newArr = arr[:]
    for i in range(N):
        newArr[i] = arr[S[i]]

    return newArr

def shuffle():
    cnt = 0
    arr = [i%3 for i in range(N)]
    firstArr = arr[:]

    while arr != P:
        arr = changeArr(arr)
        cnt += 1

        if firstArr == arr:
            return -1

    return cnt


N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))
print(shuffle())