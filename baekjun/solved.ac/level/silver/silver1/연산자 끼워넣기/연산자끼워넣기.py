import sys

# baekjoon 14888 silver1

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
answer = [-1000000001, 1000000001]


def dfs(depth, num, plus, minus, mul, div):
    if depth == N:
        answer[0] = max(answer[0], num)
        answer[1] = min(answer[1], num)
        return

    if plus: dfs(depth + 1, num + arr[depth], plus - 1, minus, mul, div)
    if minus: dfs(depth + 1, num - arr[depth], plus, minus - 1, mul, div)
    if mul: dfs(depth + 1, num * arr[depth], plus, minus, mul - 1, div)
    if div: dfs(depth + 1, int(num / arr[depth]), plus, minus, mul, div -1)


dfs(1, arr[0], op[0], op[1], op[2], op[3])
print(*answer, sep='\n')