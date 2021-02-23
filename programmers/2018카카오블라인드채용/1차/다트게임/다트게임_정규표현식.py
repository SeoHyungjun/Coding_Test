# 2021-02-18 18:33 -> 18:49

import re

def solution(dartResult):
    second = {'S':1, 'D':2, 'T':3}
    third = {'':1, '*':2, '#':-1}

    p = re.compile('(\d{1,2})([SDT])([*#]?)')
    arr = p.findall(dartResult)

    for i in range(len(arr)):
        if arr[i][2] == '*' and i != 0:
            arr[i-1] *= 2
        arr[i] = int(arr[i][0]) ** second[arr[i][1]] * third[arr[i][2]]

    return sum(arr)


dartResult = '1D2S0T'
dartResult = '1D2S#10S'
print(solution(dartResult))