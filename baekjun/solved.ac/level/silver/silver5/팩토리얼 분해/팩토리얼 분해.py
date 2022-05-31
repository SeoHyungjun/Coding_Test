import sys

N = int(sys.stdin.readline())
res = 2432902008176640000

if not N:
    N = -1
for i in range(20, 0, -1):
    res //= i
    if N >= res:
        N -= res

print('NO' if N else 'YES')