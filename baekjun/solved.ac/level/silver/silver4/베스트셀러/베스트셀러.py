import sys
from collections import defaultdict

N = int(sys.stdin.readline())
books = defaultdict(int)

max_book_cnt = 0
answer = []
for _ in range(N):
    book = sys.stdin.readline().rstrip()
    books[book] += 1

    if books[book] > max_book_cnt:
        answer = [book]
        max_book_cnt = books[book]
    elif books[book] == max_book_cnt:
        answer.append(book)

answer.sort()
print(answer[0])