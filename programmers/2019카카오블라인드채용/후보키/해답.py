def solution(relation):
    answer_list = []

    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                print(bin(i), bin(1<<k), bin(i&1<<k), 1&(1<<k))
                if i & ( 1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)
        print(tmp_set)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))