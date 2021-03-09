# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    index_skill = {}

    for i in range(len(skill)):
        index_skill[skill[i]] = i

    for tree in skill_trees:
        check_list = []
        for t in tree:
            if t in index_skill:
                check_list.append(index_skill[t])

        check = True
        if sorted(check_list) == check_list:
            for i in range(len(check_list)):
                if not(check_list[i] == check_list.index(check_list[i])):
                    check = False
            if check:
                answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))