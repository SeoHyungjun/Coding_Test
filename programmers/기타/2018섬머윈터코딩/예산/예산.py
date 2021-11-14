# 2021-03-09 22:03 -> 22:10

# def solution(d, budget):
#     sum_b = 0
#     answer = 0

#     d.sort()

#     for i in range(len(d)):
#         if sum(d[:i+1]) > budget:
#             return len(d[:i])

#     return len(d)

def solution(d, budget):
    d.sort()
    d_sum = sum(d)
    
    while d_sum > budget:
        d_sum -= d.pop()
    
    return len(d)




d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))