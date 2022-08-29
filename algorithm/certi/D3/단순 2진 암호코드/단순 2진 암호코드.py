dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

def change(num):
    result, sum = 0, 0
    for i in range(8):
        result += int(num[i])
        if not i % 2: result += int(num[i]) * 2
        sum += int(num[i])

    return sum if not result % 10 else 0

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    answer_set = set()

    for _ in range(N):
        cur = input().rstrip()
        if '1' not in cur: continue

        tmp = ''
        for i in range(len(cur)-1, -1, -1):
            if cur[i] == '0': continue
            end = i+1
            break

        for i in range(end - 56, end, 7):
            if cur[i:i + 7] not in dic: continue
            tmp += str(dic[cur[i:i + 7]])

        answer_set.add(tmp)

    flag = True
    if len(answer_set) != 1 or len(list(answer_set)[0]) != 8:
        flag = False
    
    if flag:
        print('#%d %d'%(test_case, change(list(answer_set)[0])))
    else:
        print('#%d 0'%test_case)