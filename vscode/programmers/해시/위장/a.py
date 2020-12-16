def solution(clothes):
    answer = 1

    li = {}

    for cloth in clothes:
        if cloth[1] in li:
            li[cloth[1]].append(cloth[0])
        else:
            li[cloth[1]] = [cloth[0]]

    for key in li.keys():
        answer = answer * ( len(li[key]) + 1 )

    return answer - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))