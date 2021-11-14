# 2021-03-06 21:19 -> 

def rotate(key):
    new_key = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key)-1-i] = key[i][j]
    return new_key

def check(x, y, key, lock, expendSize):
    expendList = [[0]*expendSize for _ in range(expendSize)]

    for i in range(len(key)):
        for j in range(len(key)):
            expendList[x+i][y+j] = key[i][j]
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            expendList[len(key)-1 + i][len(key)-1 + j] += lock[i][j]
            if expendList[len(key)-1 + i][len(key)-1 + j] != 1:
                return False

    return True

def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    expendSize = len(lock) + start * 2

    # 90도 회전 -> 4번 확인해야함
    for _ in range(4):
        # 시작 위치를 알려주는 i, j
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expendSize):
                    return True
        key = rotate(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))