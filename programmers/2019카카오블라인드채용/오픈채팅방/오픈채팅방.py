# 2021-02-10 14:27 -> 14:47 (20분 소요)

def solution(record):
    answer = []
    name = {}

    for re in record:
        re = re.split()
        if re[0] != 'Leave': 
            name[re[1]] = re[2]

    for re in record:
        re = re.split()
        if re[0] == 'Enter':
            answer.append(name[re[1]] + '님이 들어왔습니다.')
        elif re[0] == 'Leave':
            answer.append(name[re[1]] + '님이 나갔습니다.')

    return answer


record = ["Enter uid1234 Muzi", 
"Enter uid4567 Prodo",
"Leave uid1234",
"Enter uid1234 Prodo",
"Change uid4567 Ryan"]
print(solution(record))