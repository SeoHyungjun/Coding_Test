import sys

N, M = map(int, sys.stdin.readline().split())
box = list(map(int, sys.stdin.readline().split()))
book = list(map(int, sys.stdin.readline().split()))
answer = 0
book_index = 0

for i in range(N):
    while book_index < M and box[i] >= book[book_index]:
        box[i] -= book[book_index]
        book_index += 1

print(sum(box))