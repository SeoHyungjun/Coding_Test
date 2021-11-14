def solution(array, commands):
    answer = []
    
    for com in commands:
        new_com = array[com[0]-1:com[1]]
        new_com.sort()
        
        answer.append(new_com[com[2]-1])
    
    return answer


print(solution( [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]] ) )
