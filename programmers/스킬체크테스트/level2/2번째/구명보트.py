# 2021-03-09 18:00 ->

def solution(people, limit):
    answer = len(people)
    s_people = sorted(people, reverse=True)
    s, end = 0, len(s_people)-1

    while s < end:
        if s_people[s] + s_people[end] <= limit:
            answer -= 1
            end -= 1
        s += 1
    return answer

people = [70, 50, 80, 50]
limit = 100	
print(solution(people, limit))