# 2021-03-10 17:28 -> 17:40

def solution(n):
    answer = ''
    while n > 0:
        answer += str(n%3)
        n //= 3
    return int(answer, 3)

print(solution(45))