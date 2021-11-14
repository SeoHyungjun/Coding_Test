# 2021-03-05 (1차실패)

from itertools import combinations as combi

def solution(relation):
    len_row = len(relation) # 가로(행)의 갯수
    len_col = len(relation[0]) # 세로(열)의 갯수

    # combinations를 통해 속성(열)의 조합(중복 x) 계산
    com_list = []
    for i in range(1, len_col+1):
        com_list.extend(combi(range(len_col), i))

    # 행렬을 바꾼 리스트 생성
    change_col_row = [list(i) for i in zip(*relation)]

    unique = []
    for c in com_list:
        tmp = []
        for i in c:
            tmp.append(change_col_row[i])

        if len(  set( [ ''.join(k) for k in [list(j) for j in zip(*tmp)] ] ) ) == len_row:
            unique.append(c)
    
    duplicate = []
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if set(unique[i]) == set(unique[i]).intersection(set(unique[j])):
                duplicate.append(unique[j])

    answer = set(unique) - set(duplicate)

    return len(answer)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))