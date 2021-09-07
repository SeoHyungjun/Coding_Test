import sys
MOD = 1000000007

def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    
    half = pow(a, b//2)
    return half * half % MOD if b % 2 == 0 else half * half * a % MOD

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0

for i in range(N):
    answer += arr[i] * (pow(2, i) - pow(2, N - i - 1))

print(answer % MOD)