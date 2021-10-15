import sys

A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())

minute_add, sec = divmod(C + D, 60)
hour_add, minute = divmod(B + minute_add, 60)
hour = (A + hour_add) % 24
print(hour, minute, sec)