import sys

neon = [
    '####.##.##.####', # 0
    '..#..#..#..#..#', # 1
    '###..#####..###', # 2
    '###..####..####', # 3
    '#.##.####..#..#', # 4
    '####..###..####', # 5
    '####..####.####', # 6
    '###..#..#..#..#', # 7
    '####.#####.####', # 8
    '####.####..####'] # 9

def checkAvailnumbers(index):
    availNumbers = []
    for i in range(10): # 0 ~ 9
        avail = True
        for j in range(15):
            if arrNumber[index][j] == neon[i][j]:
                continue

            if not (arrNumber[index][j] == '.' and neon[i][j] == '#'):
                avail = False
                break

        if avail:
            availNumbers.append(i)

    return availNumbers

def checkTotalavg():
    answer = 0

    for i in range(N):
        availArr = checkAvailnumbers(i)
        
        if not availArr:
            return -1

        answer += 10**(N-i-1) * sum(availArr)/len(availArr)

    return answer

def changeInputtoNumber():
    for _ in range(5):
        inputString = sys.stdin.readline().rstrip()
        for i in range(len(inputString)):
            if (i + 1) % 4 != 0:
                arrNumber[(i+1)//4].append(inputString[i])

N = int(sys.stdin.readline())
arrNumber = [[] for _ in range(N)]

changeInputtoNumber()
print(checkTotalavg())