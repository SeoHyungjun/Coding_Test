import sys
input = sys.stdin.readline

n, m = map(int, input().split())
notlisten = []
notsee = []

for _ in range(n):
    notlisten.append(input().rstrip('\n'))

for _ in range(m):
    notsee.append(input().rstrip('\n'))

answer = set(notlisten)&set(notsee)

print(len(answer))
for i in sorted(answer):
    print(i)
