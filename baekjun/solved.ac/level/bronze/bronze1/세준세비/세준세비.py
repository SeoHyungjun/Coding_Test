import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    _ = sys.stdin.readline()
    N, M = map(int, sys.stdin.readline().split())
    S = deque(sorted(list(map(int, sys.stdin.readline().split()))))
    B = deque(sorted(list(map(int, sys.stdin.readline().split()))))

    while S and B:
        if S[0] >= B[0]:
            B.popleft()
        else:
            S.popleft()

    if not S and not B:
        print('C')
    elif S:
        print('S')
    else:
        print('B')