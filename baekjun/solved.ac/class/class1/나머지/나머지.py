import sys

li = []

for _ in range(10):
    li.append(int(sys.stdin.readline())%42)

print(len(set(li)))