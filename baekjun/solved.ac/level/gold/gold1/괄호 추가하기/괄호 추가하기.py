import sys

def cal(a, com, b):
    if com == '+': return a + b
    elif com == '-': return a - b
    else: return a * b # com == '*': return a * b

def dfs(idx, cur_sum):
    global answer

    if idx == N - 1:
        answer = max(answer, cur_sum)
        return

    if idx + 2 < N: dfs(idx + 2, cal(cur_sum, arr[idx + 1], int(arr[idx + 2])))
    if idx + 4 < N: dfs(idx + 4, cal(cur_sum, arr[idx + 1], cal(int(arr[idx + 2]), arr[idx + 3], int(arr[idx + 4]))))

N = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip()
answer = float('-inf')

dfs(0, int(arr[0]))
print(answer)