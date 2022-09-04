import sys

def change(a, b, cur):
    answer = ""
    for i in cur:
        answer += chr((a * (ord(i) - ord('A')) + b) % 26 + ord('A'))

    return answer

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        cur = sys.stdin.readline().rstrip()
        print(change(a, b, cur))

solve()