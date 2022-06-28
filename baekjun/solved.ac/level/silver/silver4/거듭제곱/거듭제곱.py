import sys

N = int(sys.stdin.readline())

answer = 0
for i, s in enumerate(reversed(bin(N).replace('0b', ''))):
    if s == '0':
        continue
    answer += 3 ** i

print(answer)