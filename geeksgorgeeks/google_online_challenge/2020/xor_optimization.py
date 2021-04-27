import sys

N = int(sys.stdin.readline())
ans = []
Q = []

xor = 0
for _ in range(N):
    Q.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(Q)-1, -1, -1):
    if Q[i][0] == 0:
        ans.append(Q[i][1]^xor)

    else:
        xor ^= Q[i][1]
ans.append(xor)
print(sorted(ans))
"""
5
0 4
0 2
1 4
0 5
1 8
"""