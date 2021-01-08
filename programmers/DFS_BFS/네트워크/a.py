def solution(n, computers):
    answer = 0

    visit = [0 for i in range(n)]

    def dfs(i):
        #print(i)
        nonlocal n, visit, computers
        visit[i] = 1

        for j in range(n):
            if visit[j] == 0 and computers[i][j] == 1:
                dfs(j)

    for i in range(n):
        if visit[i] == 0:
            dfs(i)
            answer += 1

    return answer





print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 0, 1]]))