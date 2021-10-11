import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

def checkSink(groupScc):
    answer = []
    sccNum = {}
    for index, scc in enumerate(groupScc):
        for node in scc:
            sccNum[node] = index

    for scc in groupScc:
        bottomAvail = True
        for node in scc:
            if bottomAvail:
                for next in forwardGraph[node]:
                    if sccNum[node] != sccNum[next]:
                        bottomAvail = False
                        break
        if bottomAvail:
            answer += scc

    return answer

def forwardDfs(cur):
    visited.add(cur)

    for next in forwardGraph[cur]:
        if next not in visited:
            forwardDfs(next)

    stack.append(cur)

def reverseDfs(cur, scc):
    visited.add(cur)
    scc.append(cur)

    for next in reverseGraph[cur]:
        if next not in visited:
            reverseDfs(next, scc)

    return scc

def kosaraju():
    global visited
    groupScc = []

    for i in range(1, N+1):
        if i not in visited:
            forwardDfs(i)

    visited = set()
    while stack:
        scc = []
        cur = stack.pop()

        if cur in visited:
            continue

        groupScc.append(sorted(reverseDfs(cur, scc)))

    return sorted(groupScc)

while True:
    firstInput = sys.stdin.readline().rstrip()

    if len(firstInput) == 1 and firstInput == '0':
        break

    N, M = map(int, firstInput.split())
    forwardGraph = defaultdict(list)
    reverseGraph = defaultdict(list)

    edge = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        forwardGraph[edge[2*i]].append(edge[2*i+1])
        reverseGraph[edge[2*i+1]].append(edge[2*i])

    visited = set()
    stack = []
    groupScc = kosaraju()

    print(*checkSink(groupScc))