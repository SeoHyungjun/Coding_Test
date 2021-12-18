import sys

in_train = 0
answer = 0
for _ in range(10):
    minus, plus = map(int, sys.stdin.readline().split())
    in_train += plus - minus
    answer = max(answer, in_train)

print(answer)