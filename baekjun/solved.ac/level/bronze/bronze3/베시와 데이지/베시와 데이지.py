import sys

Bx, By = map(int, sys.stdin.readline().split())
Dx, Dy = map(int, sys.stdin.readline().split())
Jx, Jy = map(int, sys.stdin.readline().split())
B = max(abs(Jx-Bx), abs(Jy-By))
D = abs(Jx-Dx) + abs(Jy-Dy)
if B == D:
    print("tie")
elif B < D:
    print("bessie")
else:
    print("daisy")