# 2021-03-04 19:51 -> 20:13

import re

def solution(s):
    answer = []

    a = sorted([list(map(int, i.replace('{', '').replace('}', '').split(','))) for i in re.split('},{', s)], key = lambda x: len(x))
    
    
    for i in a:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer


s = '{{2},{2,1},{2,1,3},{2,1,3,4}}'
print(solution(s))