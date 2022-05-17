import sys
from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
memo = {}

def search_board(diff):
    queue = deque()

    for i in range(min_val, max_val - diff + 1):
        start, end = i, i + diff

        if (start, end) in memo:
            if memo[(start, end)]:
                return True
            else:
                continue

        if not (start <= board[0][0] <= end):
            continue

        queue.append((0, 0))
        visit = set()
        visit.add((0, 0))

        while queue:
            x, y = queue.popleft()
            if (x, y) == (N-1, N-1):
                memo[(start, end)] = True
                return True

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visit and start <= board[nx][ny] <= end:
                    queue.append((nx, ny))
                    visit.add((nx, ny))

        memo[(start, end)] = False
    return False


def binary_search(left, right):
    while left < right:
        mid = (left + right)//2

        if search_board(mid):
            right = mid
        else:
            left = mid + 1

    return right

N = int(sys.stdin.readline())
board = []
min_val, max_val = float('inf'), 0
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    min_val = min(min_val, min(board[-1]))
    max_val = max(max_val, max(board[-1]))

print(binary_search(0, max_val - min_val))