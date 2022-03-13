import sys

N = int(sys.stdin.readline())

seated = set()
answer = 0
for want in map(int, sys.stdin.readline().split()):
    if want in seated:
        answer += 1
    else:
        seated.add(want)

print(answer)