# 2021-02-18 18:54 -> 19:42

import re

def solution(files):
    answer = []
    arr = {}

    p = re.compile('(\d{1,5})')
    #p = re.compile('([a-zA-Z]+)(\d{1,5})([.-]*)')

    for i, file in enumerate(files):
        arr[file] = p.split(file)
        arr[file][2] = ''.join(arr[file][2:])
        arr[file] = arr[file][:3]
        

    return sorted(arr.keys(), key = lambda x : (arr[x][0].lower(), int(arr[x][1])*-1))





files = ['foo9.txt', 'foo010bar020.zip', 'F-15']
print(solution(files))