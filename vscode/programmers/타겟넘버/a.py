def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(where, sum):
        if n == where:
            if sum == target:
                nonlocal answer
                answer += 1
        else:
            dfs(where+1, sum + numbers[where])
            dfs(where+1, sum - numbers[where])

    dfs(0, 0)

    return answer









print(solution([1, 1, 1, 1, 1], 3))