import sys

def solve():
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    arr.append(arr[0])

    answer = 0
    for i in range(len(arr)-1):
        answer += arr[i][0]*arr[i+1][1] - arr[i][1]*arr[i+1][0]

    print(round(abs(answer/2), 1))

solve()