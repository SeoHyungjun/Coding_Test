# 2021-02-17 18:07 -> 18:20

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        an = bin(int(arr1[i])|int(arr2[i])).lstrip('0b')
        head = '0' * (n - len(an))

        answer.append((head + an).replace('1', '#').replace('0', ' '))

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))