max_sum = 0
finish = 0

def solution(n, passenger, train):
    global max_sum, finish
    graph = [[float('inf')] * n for _ in range(n)]

    for st, en in train:
        graph[st-1][en-1] = passenger[st-1]
        graph[en-1][st-1] = passenger[st-1]

    visit = [True] * n
    visit[0] = False

    def dfs(cur, sum_passenger):
        print(cur+1, sum_passenger, visit)
        global max_sum, finish
        if sum_passenger > max_sum:
            max_sum = sum_passenger
            finish = cur
        if sum_passenger == max_sum:
            finish = max(cur, finish)

        for i in range(len(graph[cur])):
            if visit[i] and graph[cur][i] != float('inf'):
                visit[i] = False
                dfs(i, sum_passenger+passenger[i])
                visit[i] = True

    dfs(0, passenger[0])
    print([finish+1, max_sum])

    # visit = [True] * n
    # visit[0] = False
    # stack = [(0, passenger[0])]
    # max_sum = 0
    # finish = 0

    # while stack:
    #     cur, sum_passenger = stack.pop()
    #     if sum_passenger >= max_sum:
    #         max_sum = sum_passenger
    #         if sum_passenger == max_sum:
    #             finish = max(cur, finish)
        
    #     for i in range(len(graph[cur])):
    #         if visit[i] and graph[cur][i] != float('inf'):
    #             visit[i] = False
    #             stack.append((i, sum_passenger + passenger[i]))

    return [finish+1, max_sum]



print(solution(6, [1,1,1,1,1,1], [[1,2], [1,3], [1,4], [3,5], [3,6], [2,3]]))
print(solution(4, [2,1,2,2], [[1,2], [1,3], [2,4]]))
print(solution(5, [1,1,2,3,4], [[1,2], [1,3], [1,4], [1,5]]))