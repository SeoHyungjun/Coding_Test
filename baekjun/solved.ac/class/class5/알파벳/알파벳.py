import sys
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = set([(0, 0, arr[0][0])])
    answer = 1

    while queue:
        print(queue)
        x, y, check = queue.pop()

        for dx, dy in dir:
            if 0 <= x + dx < R and 0 <= y + dy < C and arr[x+dx][y+dy] not in check:
                queue.add((x+dx, y+dy, check + arr[x+dx][y+dy]))
                answer = max(answer, len(check + arr[x+dx][y+dy]))
    
    return answer

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

print(bfs())