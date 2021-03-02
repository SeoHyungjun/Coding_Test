#2021-03-02 16:05 -> 17:05

def change_num(num, zinbub):
    result = ''
    over = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    if num == 0:
        return '0'
    while num != 0:
        if num%zinbub < 10:
            result += str(num%zinbub)
        else:
            result += over[num%zinbub]
        num //= zinbub

    return result[::-1]

def solution(n, t, m, p):
    answer = ''

    # n 진법, 대답 길이 t, 총 인원 m, 튜브 순서 p
    result = ''
    start = 0
    
    while m*t > len(result):
        result += change_num(start, n)
        start += 1
    
    for i in range(p-1, t*m + p - 1, m):
        answer += result[i]


    return answer


#print(solution(2, 4, 2, 1))
#print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))