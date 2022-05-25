import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())
    if N == 0:
        return 0
    
    books = list(map(int, sys.stdin.readline().split()))

    answer = 0
    cur = 0
    for i in books:
        cur += i
        if cur > M:
            answer += 1
            cur = i

    return answer + 1

print(solve())