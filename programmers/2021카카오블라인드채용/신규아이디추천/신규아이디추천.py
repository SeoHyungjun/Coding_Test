# 2021-02-08 18:57 -> 19:17 (총 20분 소요)

def solution(new_id):
    answer = ''
    
    # 단계 1
    new_id = new_id.lower()
    
    # 단계 2
    for i in range(len(new_id)):
        if 'a' <= new_id[i] <= 'z' or '0' <= new_id[i] <= '9' or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':  
            answer += new_id[i]

    # 단계 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 단계 4
    answer = answer.strip('.')

    # 단계 5
    if answer == '':
        answer = 'a'

    # 단계 6
    if len(answer) >= 16:
        if answer[14] == '.':
            answer = answer[0:14]
        else:
            answer = answer[0:15]
        
    # 단계 7
    while len(answer) <= 2:
        answer += answer[len(answer)-1]

    return answer



new_id = "...!@BaT#*..y.abcdefghijklm"
result = solution(new_id)
print(result)
