import sys

N, L = map(int, sys.stdin.readline().split())

num, answer = 0, 0
while answer < N:
    num += 1
    if str(L) in str(num):
        continue
    answer += 1
    
print(num)