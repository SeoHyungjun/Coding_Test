import sys

T = int(sys.stdin.readline())
for _ in range(T):
    pw = sys.stdin.readline().rstrip()
    if 6 <= len(pw) <= 9:
        print('yes')
    else:
        print('no')