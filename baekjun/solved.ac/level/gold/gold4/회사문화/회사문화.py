# 18:40 -> 19:09

import sys

N, M = map(int, sys.stdin.readline().split())

person = [0]*N
dic = {}

up_person = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    dic[i] = up_person[i] - 1

for _ in range(M):
    S, W = map(int, sys.stdin.readline().split())
    person[S-1] += W

for i in range(1, N):
    person[i] += person[dic[i]]

for i in person:
    print(i, end = ' ')