import sys

plus, minus = map(int, sys.stdin.readline().split())

if plus - minus < 0 or (plus - minus) % 2 != 0:
    print(-1)
else:
    mk = (plus + minus) // 2
    afc = plus - mk
    print(max(mk, afc), min(mk, afc))