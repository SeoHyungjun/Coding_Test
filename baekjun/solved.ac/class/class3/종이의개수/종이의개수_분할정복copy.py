import sys

N = int(sys.stdin.readline())
matrix = []
result = [0] * 3 

for _ in range(N): 
    matrix.append(list(map(int, sys.stdin.readline().split())))
    
def check(x, y, size): 
    temp = matrix[x][y] 
    for i in range(size): 
        for j in range(size): 
            if temp != matrix[x+i][y+i]: 
                return False 
    return True 
            
def divide(x, y, size):
    if check(x, y, size): 
        result[matrix[x][y] + 1] += 1 
    else: 
        for i in range(3): 
            for j in range(3): 
                divide(x + i*size//3, y + j*size//3, size//3)
                
divide(0, 0, N) 
for i in range(3): 
    print(result[i])
