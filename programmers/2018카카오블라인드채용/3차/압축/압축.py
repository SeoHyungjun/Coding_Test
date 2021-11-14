# 2021-02-19 21:14 -> 21:47

def make_dic():
    dic = {}
    for i in range(0, ord('Z')-ord('A')+1):
        dic[chr(ord('A')+i)] = i+1
    return dic

def solution(msg):
    answer = []
    dic = make_dic()
    cur = ''
    new = 27
    msg = list(msg)
    print(dic)

    for i in range(len(msg)):
        cur += msg[i]
        print(cur)

        if i+1 < len(msg) and cur + msg[i+1] not in dic.keys():
            #print(cur)
            dic[cur + msg[i+1]] = new
            new += 1
            answer.append(dic[cur])
            cur = ''
        if i == len(msg) - 1:
            answer.append(dic[cur])
    


    return answer



msg = 'KAKAO'
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))