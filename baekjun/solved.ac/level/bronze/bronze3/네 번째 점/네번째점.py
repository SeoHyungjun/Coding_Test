import sys

x_set = set()
y_set = set()
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())

    x_set.add(x) if x not in x_set else x_set.remove(x)
    y_set.add(y) if y not in y_set else y_set.remove(y)

print(*x_set, *y_set)
