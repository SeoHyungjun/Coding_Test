# 21-02-09 18:51 -> 

from itertools import combinations, product
import bisect

changes = []
tmp = []

def replacement(ch, data):
    for i in range(4):
        if ch[i]:
            data[i] = '-'


def solution(info, query):
    answer = []
    changes_arr = {}

    # 중복 순열을 사용하여 16가지의 경우의 수 생성
    #changes = list(product([True, False], repeat=4))
    changes = list(product([True, False], repeat=4))

    for data in info:
        data = data.split()
        score = int(data[-1])
        data = data[:4]

        for ch in changes:
            _data = data[:]
            replacement(ch, _data)
            _data = ''.join(_data)

            if _data not in changes_arr.keys():
                changes_arr[_data] = [score]
            else:
                changes_arr[_data].append(score)

    for i in changes_arr.keys():
        changes_arr[i].sort()

    for qu in query:
        qu = qu.replace('and', '').split()
        score = int(qu[-1])
        qu = ''.join(qu[:4])

        if qu not in changes_arr.keys():
            answer.append(0)
        else:
            count = len(changes_arr[qu]) - bisect.bisect_left(changes_arr[qu], score, lo = 0, hi = len(changes_arr[qu]))
            answer.append(count)

    return answer



info = ["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150",
"- and - and - and - 0",
"a and b and c and d 1000"]

print(solution(info, query))