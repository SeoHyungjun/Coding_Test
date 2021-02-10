# 2021-02-10 14:52 -> 

def solution(N, stages):
    answer = []
    stage_pass_user = {}
    for i in range(N):
        stage_pass_user[i+1] = 0
    

    for st in stages:
        for i in range(1, st):
            stage_pass_user[i] += 1
    

    print(stage_pass_user)
    for st, count in stage_pass_user.items():
        if stages.count(st) + count != 0:
            stage_pass_user[st] = stages.count(st) / (stages.count(st) + count)
        else:
            stage_pass_user[st] = 0
    print(stage_pass_user)

    for i in sorted(stage_pass_user.items(), key = lambda x : (x[1], -1*x[0]), reverse = True):
        answer.append(i[0])
    
    return answer




N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = [1, 2, 2, 1, 3]
stages = [6,6,6,6,6]
print(solution(N, stages))