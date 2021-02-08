# 2021-02-08 19:52 -> 
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        course_dict = {}
        for order in orders:
            if c <= len(order):
                combi = combinations(order, c)
                for com in combi:
                    food = "".join(sorted(com))
                    
                    if food not in course_dict:
                        course_dict[food] = 1
                    else:
                        course_dict[food] += 1

        result = [a for a, b in course_dict.items() if max(course_dict.values()) == b and b >= 2]
        answer += result

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))