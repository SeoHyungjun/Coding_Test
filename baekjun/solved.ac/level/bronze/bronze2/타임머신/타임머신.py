import sys

a, b, c = map(int, sys.stdin.readline().split(':'))

answer = 0

if 1 <= a <= 12 and 0 <= b <= 59 and 0 <= c <= 59:
    answer += 1
if 1 <= a <= 12 and 0 <= c <= 59 and 0 <= b <= 59:
    answer += 1
if 1 <= b <= 12 and 0 <= a <= 59 and 0 <= c <= 59:
    answer += 1
if 1 <= b <= 12 and 0 <= c <= 59 and 0 <= a <= 59:
    answer += 1
if 1 <= c <= 12 and 0 <= a <= 59 and 0 <= b <= 59:
    answer += 1
if 1 <= c <= 12 and 0 <= b <= 59 and 0 <= a <= 59:
    answer += 1

print(answer)