import sys
from collections import defaultdict

def changeLast(sortedAlpha, firstCheckset):
    if sortedAlpha[-1] not in firstCheckset:
        return sortedAlpha

    for i in range(9, -1, -1):
        if sortedAlpha[i] not in firstCheckset:
            changeIndex = i
            break
    
    sortedAlpha = ''.join(sortedAlpha)
    return list(sortedAlpha[:changeIndex] + sortedAlpha[changeIndex+1:] + sortedAlpha[changeIndex])

def maxSum():
    alpha = defaultdict(int)
    firstCheckset = set()

    for i in range(len(arr)):
        multiNum = 10**(len(arr[i]) - 1)
        firstCheckset.add(arr[i][0])
        for j in range(len(arr[i])):
            alpha[arr[i][j]] += multiNum
            multiNum //= 10

    sortedAlpha = sorted(alpha.keys(), key = lambda x : (-1 * alpha[x], x))
    if len(sortedAlpha) == 10:
        sortedAlpha = changeLast(sortedAlpha, firstCheckset)

    answer = 0
    for i in range(len(sortedAlpha)):
        answer += alpha[sortedAlpha[i]] * (9 - i)

    return answer

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]

print(maxSum())