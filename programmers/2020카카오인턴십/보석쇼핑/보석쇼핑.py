# 2021-03-11 16:25 ->

def solution(gems):
    answer  = [1, len(gems)]

    len_gems = len(gems) # 입력된 배열의 수
    cnt_gems = len(set(gems)) # 보석의 종류 수

    start, end = 0, 0
    dic_gems = {} # 현재 구간의 보석 수

    while True: # 뒤의 인덱스, 8개 입력될경우 7까지이므로 <로..
        print(start, end, dic_gems, answer)

        if len(dic_gems) == cnt_gems: # 현재 구간의 보석 종류가 총 보석의 종류 수와 같다면
            # 최솟값 비교
            answer = min(answer, [start+1, end], key = lambda x : x[1] - x[0])

            # start 위치의 보석 제거
            if dic_gems[gems[start]] == 1: # 0이 되므로 딕셔너리에서 제거
                del dic_gems[gems[start]]
            else: # 1개만 감소시키기
                dic_gems[gems[start]] -= 1
            # start를 증가시켜버리기
            start += 1

        else: # 현재 구간의 보석 종류가 총 보석의 종류 수와 다르면 == 적으면
            end += 1
            if end > len_gems:
                break
            # end 위치의 보석 추가하기
            if gems[end-1] in dic_gems: # 이미 딕셔너리 안에 있다면 증가
                dic_gems[gems[end-1]] += 1
            else: # 딕셔너리에 새로 추가
                dic_gems[gems[end-1]] = 1
            # end를 증가시키기

    return answer
    


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems = ['DIA', 'EM', 'EM', 'RUB', 'DIA']
print(solution(gems))