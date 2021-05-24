import sys
from math import gcd
MOD = 1000000007

M = int(sys.stdin.readline())
answer = 0

def multi(a, squared):
    if squared == 1:
        return a

    if squared % 2:
        return a * multi(a, squared-1) % MOD

    x = multi(a, squared//2) % MOD
    return x*x%MOD

for _ in range(M):
    a, b= map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    a //= g
    b //= g
    
    answer += b*multi(a, MOD-2)%MOD
    answer %= MOD

print(answer)