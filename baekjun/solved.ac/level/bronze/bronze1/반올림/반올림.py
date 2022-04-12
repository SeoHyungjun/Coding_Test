import sys

N = list(sys.stdin.readline().rstrip())

check = 10
index = len(N) - 1

while int(''.join(N)) >= check:
    for i in range(index, 0, -1):
        if int(N[i]) >= 5:
            N[i-1] = str(int(N[i-1]) + 1)
        N[i] = '0'

    check *= 10
    index -= 1

print(''.join(N))