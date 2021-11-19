import sys

arr = [sys.stdin.readline().rstrip() for _ in range(6)]
answer = arr.count('W')

if answer > 4:
    print(1)
elif answer > 2:
    print(2)
elif answer > 0:
    print(3)
else:
    print(-1)