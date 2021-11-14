# 210119 18:17 -> 18:44

from collections import deque

def check_word(a, b):
    diff_cnt = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diff_cnt += 1
    
    if diff_cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0))

    while queue:
        cur, cnt = queue.popleft()
        print(cur, cnt, queue)

        if cur == target:
            return cnt

        for word in words:
            if check_word(cur, word):
                queue.append((word, cnt+1))
                words.remove(word)

    return 0



a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(a,b,c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log"]

print(solution(a,b,c))