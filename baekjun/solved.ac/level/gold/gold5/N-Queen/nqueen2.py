import sys

def possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(x):
    global result
    
    if x == n:
        result += 1
    
    else:
        for i in range(n):
            row[x] = i
            if possible(x):
                dfs(x+1)

n = int(sys.stdin.readline())
row = [0] * n
result = 0
dfs(0)
print(result)