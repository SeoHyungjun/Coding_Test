import sys
from collections import defaultdict

dic = defaultdict(int)

N = int(sys.stdin.readline())
for _ in range(N):
    tmp = sys.stdin.readline().rstrip()

    if len(tmp) == 1 or len(tmp) == 2:
        dic[tmp] = 1
    else:
        key = tmp[0] + tmp[-1] + ''.join(sorted(list(tmp[1:-1])))
        dic[key] += 1

M = int(sys.stdin.readline())
for _ in range(M):
    S = sys.stdin.readline().rstrip().split()
    
    answer = 1

    for tmp in S:
        if len(tmp) == 1 or len(tmp) == 2:
            answer *= dic[tmp]
        else:
            answer *= dic[tmp[0] + tmp[-1] + ''.join(sorted(list(tmp[1:-1])))]

    print(answer)
"""
3
ababa
aabba
abcaa
2
ababa
ababa abcaa

2
2

14
bakers
brakes
breaks
binary
brainy
baggers
beggars
and
in
the
blowed
bowled
barn
bran
1
brainy bakers and beggars bowled in the barn

48
"""