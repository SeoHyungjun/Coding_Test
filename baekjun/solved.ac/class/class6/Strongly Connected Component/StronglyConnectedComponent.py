# scc 알고리즘
# scc 알고리즘은 크게 Kosaraju 알고리즘과 Tarjan 알고리즘이 있다

# Kosaraju 알고리즘은
# 순방향 및 역방향 그래프와 스택이 필요하다.
# 순방향 그래프에서 dfs를 통해 이어진 노드 중 방문하지 않은 노드가 없을때까지 방문한 뒤
# 스택에 역순으로 저장한다.
# 그리고 스택에서 pop하면서 pop된 노드에서 역방향으로 방문하면서 더이상 방문할 수 없을경우까지를 scc로 분류한다.

# 블로거의 설명 출처: https://ca.ramel.be/166?category=935131 [MemoLOG]
# 코사라주 알고리즘을 수행하기 위해서는 먼저 문제에 주어진 정방향 그래프와, 각 그래프의 방향이 정반대인 역방향 그래프 두가지를 준비해야한다.
# 먼저 정방향 그래프를 이용하여 모든 그래프 상에서 dfs 탐색을 수행하고, 
# dfs 탐색이 종료되는 순서대로 stack에 append 해준다. 
# 이후 해당 stack에서 요소들을 한개씩 pop하여 순서대로 역방향 dfs를 수행하고, 
# 한번 수행에 탐색되는 모든 정점들을 SCC로 묶는다. 
# 스택이 빌 때까지 이 작업을 계속해주면 SCC를 구할 수 있다.

import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def dfs(cur):
    visited.add(cur)

    for next in forwardGraph[cur]:
        if next not in visited:
            dfs(next)
    stack.append(cur)

def reverseDfs(cur, scc):
    visited.add(cur)
    scc.append(cur)

    for next in reverseGraph[cur]:
        if next not in visited:
            scc = reverseDfs(next, scc)
    return scc

def kosaraju():
    global visited
    answer = []
    # 정방향 그래프를 돌면서 dfs 실행
    for i in range(1, V+1):
        if i not in visited:
            dfs(i)

    visited = set()
    while stack:
        scc = []
        cur = stack.pop()

        if cur in visited:
            continue

        answer.append(sorted(reverseDfs(cur, scc)))
    return answer

V, E = map(int, sys.stdin.readline().split())
forwardGraph = defaultdict(list)
reverseGraph = defaultdict(list)

for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    forwardGraph[A].append(B)
    reverseGraph[B].append(A)

stack = []
visited = set()
answer = kosaraju()

print(len(answer))
for line in sorted(answer):
    print(*line, sep = ' ', end = ' -1\n')