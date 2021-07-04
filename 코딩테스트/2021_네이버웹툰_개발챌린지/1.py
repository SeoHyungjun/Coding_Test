def solution(lottery):
    answer = -1

    dic = {}
    for i in range(1, 1001):
        dic[i] = [False, 0]

    count = []
    # i 아이디, j 당첨여부
    for i, j in lottery:
        if dic[i][0] == False:
            dic[i][1] += 1

            if j == 1:
                dic[i][0] = True
                count.append(dic[i][1])
        
    
    if not count:
        answer = 0
    else:
        answer = sum(count)//len(count)

    return answer


print(solution([[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]))
print(solution([[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]]))
print(solution([[1,0],[2,0],[3,0]]))