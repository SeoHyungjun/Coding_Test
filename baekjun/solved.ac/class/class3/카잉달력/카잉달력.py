import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    #answer%n = x
    #answer%m = y 
    ans = -1
    if n > m:
        m,n,x,y = n,m,y,x
    for i in range(x, m*n+1, m):
        if (i-y) % n == 0:
            ans = i
            break

    print(ans)