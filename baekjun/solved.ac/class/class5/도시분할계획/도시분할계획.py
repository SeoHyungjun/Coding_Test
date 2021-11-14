import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())

    edge = []
    parent = [i for i in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        edge.append((c, a, b))

    edge.sort()

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    answer = []
    for c, a, b in edge:
        if find(a) != find(b):
            union(a, b)
            answer.append(c)

    print(sum(answer[:-1]))

solve()
