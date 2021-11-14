import sys

def distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def solve():
    N = int(sys.stdin.readline())
    house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    answer, min_length = 0, float('inf')

    for i in range(N):
        max_length = 0
        for j in range(N):
            max_length = max(max_length, distance(house[i], house[j]))

        if max_length < min_length:
            answer, min_length = i, max_length

    print(*house[answer])

solve()