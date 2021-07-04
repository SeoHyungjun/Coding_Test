def solution(grid):
    width, height = len(grid[0]), len(grid)

    for i in range(1, height):
        grid[i][0] += grid[i-1][0]

    for i in range(1, width):
        grid[0][i] += grid[0][i-1]

    for i in range(1, height):
        for j in range(1, width):
            grid[i][j] = min(grid[i-1][j] + grid[i][j], grid[i][j-1] + grid[i][j])

    return grid[height-1][width-1]

print(solution([ [1, 2], [3, 4] ]))
print(solution([ [1, 8, 3, 2], [7, 4, 6, 5] ]))