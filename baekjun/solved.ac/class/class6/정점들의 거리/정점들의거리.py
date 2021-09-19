import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10**6)

def query(a, b):
    tmp_a, tmp_b = a, b

    if depth[a] != depth[b]:
        # a < b가 되도록 스왑
        a, b = min(a, b, key = lambda x : depth[x]), max(a, b, key = lambda x : depth[x])
        # b를 올려서 depth를 맞춘다
        for i in range(MAX_DEPTH, -1, -1):
            if depth[a] <= depth[ancestor[b][i]]:
                b = ancestor[b][i]

    lca = a
    if a != b:
        for i in range(MAX_DEPTH, -1, -1):
            if ancestor[a][i] != ancestor[b][i]:
                a = ancestor[a][i]
                b = ancestor[b][i]
            lca = ancestor[a][i]

    print(distance_from_root[tmp_a] + distance_from_root[tmp_b] - 2*distance_from_root[lca])

def make_tree(cur, parent, distance_from_parent): # 현재노드, 부모노드, 부모노드와 현재 노드의 거리
    depth[cur] = depth[parent] + 1 # 현재 노드의 depth는, 부모의 depth + 1

    # cur가 1이면, root와의 거리가 0 (초기값) 
    # 아닐 경우, root - 부모의 거리 + 부모와의 거리
    if cur != 1:
        distance_from_root[cur] += distance_from_root[parent] + distance_from_parent

    # cur의 1번째 부모는 parent
    ancestor[cur][0] = parent

    for i in range(1, MAX_DEPTH + 1):
        # 2^i번째 조상은 2^(i-1)번째 조상의 2^(i-1)번째 조상
        ancestor[cur][i] = ancestor[ancestor[cur][i-1]][i-1] # 예를 들면 2(2^1)번 위 조상은 1(2^0)번째 조상의 1(2^0)번째 조상

    # dfs 호출
    for next_node, cost in graph[cur]:
        if next_node == parent:
            continue
        make_tree(next_node, cur, cost)

N = int(sys.stdin.readline())
MAX_NODE = 40000 + 1 # 40000개의 노드가 들어올 수 있는데, 40000번째 리스트까지 만드려면 40001로 설정해야 함 
# MAX_NODE = N + 1
MAX_DEPTH = int(math.floor(math.log2(MAX_NODE))) # 최대 depth를 계산
depth = [0] * MAX_NODE # 각 노드의 depth 저장
ancestor = [[0]*20 for _ in range(MAX_NODE)] # 각 노드의 2^i번째 부모(조상) 저장
distance_from_root = [0] * MAX_NODE

graph = defaultdict(list)
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

depth[0] = -1 # 루트 노드는 1부터 시작, 1의 부모를 0으로 잡고 depth를 -1로 하면 1은 depth가 1로 시작
make_tree(1, 0 ,0) # 1을 루트로 잡으면, 루트의 부모는 0이 된다.

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    query(a, b)

"""
15
1 2 1
1 3 1
2 4 1
3 7 1
6 2 1
3 8 1
4 9 1
2 5 1
5 11 1
7 13 1
10 4 1
11 15 1
12 5 1
14 7 1
6
6 11
10 9
2 6
7 6
8 13
8 15
"""
"""
3
2
1
4
3
6
"""