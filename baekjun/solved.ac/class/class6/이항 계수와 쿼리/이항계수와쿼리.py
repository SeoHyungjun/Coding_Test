import sys
MOD = 1000000007

# return x^y
def pow(x, y):
    if y == 1:
        return x

    half = pow(x, y//2)
    return half * half * x % MOD if y % 2 else half * half % MOD

# 페르마 소정리
def fermats_little_theorem(num):
    return pow(num, MOD - 2) % MOD

def solve(n, k):
    return factorial[n] * fermats_little_theorem(factorial[n-k]) * fermats_little_theorem(factorial[k]) % MOD

M = int(sys.stdin.readline())
factorial = [1] * 4000001
for i in range(2, 4000001):
    factorial[i] = factorial[i-1] * i % MOD

for i in range(M):
    N, K = map(int, sys.stdin.readline().split())
    print(solve(N, K))

#  이항계수는 (n / k)는 0 <= k <= n 이므로 
# (n 
#  k) = n! / ((n-k)!*k!) = n! * ((n-k)!k!)^-1

# 페르마 소정리 : 소수 p가 있고, 정수 a가 p의 배수가 아닐 때 다음이 성립
# a^p == a(mod p) -> 양 변을 a^2로 나누면
# a^(p-2) == a^-1(mod p)

# 위 식을 a^-1(mod p) == a^(p-2)로 생각하고
# 이항계수 식으로 변환하면
# n! * ((n-k)!k!)^-1 (mod p) = n!(mod p) * (n-k)!^(p-2)(mod p) * k!^(p-2)(mod p)