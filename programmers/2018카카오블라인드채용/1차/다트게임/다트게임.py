# 2021-02-17 18:27 -> 19:04

def solution(dartResult):
    arr_index = -1
    arr = [[] for _ in range(3)]

    dartResult = dartResult.replace('10', 't')
    print(dartResult)

    for i in range(len(dartResult)):
        if dartResult[i] == 't':
            arr_index += 1
            arr[arr_index].append(10)
        else:
            if '0' <= dartResult[i] <= '9':
                arr_index += 1
            arr[arr_index].append(dartResult[i])
            

    print(arr)

    for index, each in enumerate(arr):
        each[0] = int(each[0])
        if each[1] == 'D':
            each[0] = each[0] ** 2
        elif each[1] == 'T':
            each[0] = each[0] ** 3

        if len(each) == 3:
            if each[2] == '*':
                each[0] *= 2
                if index > 0:
                    arr[index-1][0] *= 2

            elif each[2] == '#':
                each[0] *= -1


    return arr[0][0] + arr[1][0] + arr[2][0]


dartResult = '1D2S0T'
print(solution(dartResult))