import sys

finger = int(sys.stdin.readline())
cnt = int(sys.stdin.readline())

if finger in [1, 5]:
    print(8*cnt + finger-1)
else:
    print(4*cnt + 1 + (4 - finger if cnt & 1 else finger - 2))