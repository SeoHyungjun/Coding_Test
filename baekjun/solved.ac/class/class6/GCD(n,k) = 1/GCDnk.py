import sys

N = int(sys.stdin.readline())
answer = N

for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        while N % i == 0:
            N //= i

        answer -= answer / i

if N > 1:
    answer -= answer / N

print(int(answer))