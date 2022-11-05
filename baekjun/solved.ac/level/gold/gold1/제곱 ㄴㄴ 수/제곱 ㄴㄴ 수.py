import sys

def solve():
    global answer
    for i in range(2, int(b**0.5) + 1):
        cur = i * i
        for j in range(a // cur * cur, b + 1, cur):
            if j - a < 0 or check[j - a]: continue
            check[j - a] = True
            answer -= 1

a, b = map(int, sys.stdin.readline().split())
answer = b - a + 1
check = [False] * answer

solve()
print(answer)