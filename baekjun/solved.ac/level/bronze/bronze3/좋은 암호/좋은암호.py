import sys

K, L = map(int, sys.stdin.readline().split())

answer = 'GOOD'
for i in range(2, L):
    if K % i == 0:
        answer = 'BAD ' + str(i)
        break

print(answer)