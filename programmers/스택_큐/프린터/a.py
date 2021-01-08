def solution(priorities, location):
    answer = 1

    while priorities:
        print(location, priorities)
        cur = priorities.pop(0)

        if (not priorities) or cur >= max(priorities):
            if location == 0:
                break
            else:
                answer += 1
        else:
            priorities.append(cur)
            
            if location == 0:
                location = len(priorities) - 1
                continue

        location -= 1



    return answer


#print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))