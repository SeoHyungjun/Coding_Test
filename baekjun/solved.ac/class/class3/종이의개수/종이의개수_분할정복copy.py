import sys

N = int(sys.stdin.readline())
matrix = []
result = [0] * 3 

for _ in range(N): 
    matrix.append(list(map(int, sys.stdin.readline().split())))

def check(x, y, n): 
    temp = matrix[x][y] 
    for i in range(n): 
        for j in range(n): 
            if temp != matrix[x+i][y+j]: 
                return False 
    return True 
            
def divide(x, y, n):
    if check(x, y, n): 
        result[matrix[x][y] + 1] += 1 
    else: 
        for i in range(3): 
            for j in range(3): 
                divide(x + i*n//3, y + j*n//3, n//3)

    return

divide(0, 0, N) 
for i in range(3): 
    print(result[i])
