import sys

N = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

li.sort()

for i in range(1, len(li)):
    li[i] += li[i-1]

print(sum(li))