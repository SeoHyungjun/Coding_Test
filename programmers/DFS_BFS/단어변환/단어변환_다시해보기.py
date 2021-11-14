from collections import deque
import copy

def CHECK(a, b):
    len_word = len(a)
    cnt = 0
    for i in range(len_word):
        if a[i] == b[i]:
            cnt += 1
    
    if len_word - 1 == cnt:
        return True
    else:
        return False

def BFS(begin, target, words):
    queue = deque()
    queue.append((begin, [begin]))

    while queue:
        cur, visit = queue.popleft()
        if cur == target:
            return len(visit) - 1

        for word in words:
            if word not in visit and CHECK(cur, word):
                new_visit = copy.deepcopy(visit)
                new_visit.append(word)
                queue.append((word, new_visit))

    return 0

def solution(begin, target, words):
    return BFS(begin, target, words)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))