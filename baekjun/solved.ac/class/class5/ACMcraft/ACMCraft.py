import sys
import heapq

def topology_sort(end, queue, build_time, building, indegree, N):
    for i in range(N):
        if indegree[i] == 0:
            heapq.heappush(queue, (build_time[i], i))

    while queue:
        cost, cur = heapq.heappop(queue)

        if cur == end:
            return cost

        for i in building[cur]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(queue, (cost + build_time[i], i))

def main():
    global queue
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())
        build_time = list(map(int, sys.stdin.readline().split()))

        building = [[] for i in range(N)]
        indegree = [0] * N

        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            building[X-1].append(Y-1)
            indegree[Y-1] += 1

        W = int(sys.stdin.readline())

        print(topology_sort(W-1, queue, build_time, building, indegree, N))

queue = []
main()