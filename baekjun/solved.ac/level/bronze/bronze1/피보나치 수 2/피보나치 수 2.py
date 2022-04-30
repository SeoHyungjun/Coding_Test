import sys

fibo = [0, 1] + [0]*89
for i in range(2, 91):
    fibo[i] = fibo[i-1] + fibo[i-2]

N = int(sys.stdin.readline())
print(fibo[N])