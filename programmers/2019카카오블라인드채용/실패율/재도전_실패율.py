def solution(N, stages):
    ratio = {}
    leave_person = len(stages)

    # 딕셔너리 초기화
    for i in range(1, N+1):
        cur_person = stages.count(i)
        if leave_person != 0:
            ratio[i] = cur_person / leave_person
        else:
            ratio[i] = 0

        leave_person -= cur_person

    return sorted(ratio, key = lambda x : ratio[x], reverse = True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))