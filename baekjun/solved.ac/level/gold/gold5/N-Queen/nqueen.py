# 2021-03-16 17:17 -> 18:23
# 백준 python3 시간초과
# 백준 pypy3 성공

# n queen -> back tracking - > dfs 방식 + 가지치기

import sys
answer = 0

def dfs(in_queen, n, rd, ld):
    global answer
    print(in_queen, rd, ld)
    if len(in_queen) == n:
        answer += 1
        return

    for i in range(n):
        # 같은 rox는 항상 없는 상태
        # 같은 col인지 확인 + 같은 대각선에 있는지 확인 (우측아래로가는, 좌측 아래로가는) 
        if i not in in_queen and rd[len(in_queen)-i] == 0 and ld[len(in_queen)+i] == 0:
                    rd[len(in_queen)-i] = 1
                    ld[len(in_queen)+i] = 1
                    in_queen.append(i)
                    dfs(in_queen, n, rd, ld)
                    in_queen.pop()
                    rd[len(in_queen)-i] = 0
                    ld[len(in_queen)+i] = 0

n = int(sys.stdin.readline())
answer = 0
in_queen = []
rd, ld = {}, {}
for i in range(-n+1, n):
    rd[i] = 0
for i in range(2*n):
    ld[i] = 0

dfs(in_queen, n, rd, ld)

print(answer)