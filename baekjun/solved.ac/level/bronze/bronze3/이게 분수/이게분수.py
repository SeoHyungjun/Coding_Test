import sys

def rotate(arr):
    new_arr = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            new_arr[i][j] = arr[2-1-j][i]

    return new_arr

def check_value(arr):
    return arr[0][0]/arr[1][0] + arr[0][1]/arr[1][1]

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
answer, max_value = 0, check_value(arr)

for i in range(1, 4): 
    arr = rotate(arr)

    if check_value(arr) > max_value:
        answer, max_value = i, check_value(arr)

print(answer)