# 2021-03-09 18:25 -> 19:29

from itertools import permutations as perm

def check(perm_g, banned):
    for p, b in zip(perm_g, banned):
        if len(p) != len(b):
            return False
        
        for i in range(len(p)):
            if b[i] != '*' and p[i] != b[i]:
                return False

    return True



def solution(user_id, banned_id):
    answer = []

    for perm_g in perm(user_id, len(banned_id)):
        if check(perm_g, banned_id):
            if sorted(perm_g) not in answer:
                answer.append(sorted(perm_g))

    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))