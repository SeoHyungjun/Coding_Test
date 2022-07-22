import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
final = list(map(str, sys.stdin.readline().strip()))
start = sorted(final)

left = 0
right = []
for _ in range(m):
    ladder = list(map(str,input().strip()))
    
    if ladder == ['?' for _ in range(n-1)]:
        left = right
        right = []
        continue
    right.append(ladder)

while left:
    ladder = left.pop(0)
    for i in range(n-1):
        if ladder[i] == '-':
            start[i], start[i+1] = start[i+1], start[i] 

while right:
    ladder = right.pop()
    for j in range(n-1):
        if ladder[j] == '-':
            final[j], final[j+1] = final[j+1], final[j]

ans = ['*' for _ in range(n-1)]
for k in range(n-1):
    if start[k] == final[k+1] and start[k+1] == final[k]:
        ans[k] = '-'
        start[k], start[k+1] = start[k+1], start[k]

if start != final:
    ans = ['x' for _ in range(n-1)]
print(''.join(ans))