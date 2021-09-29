import sys
from collections import deque

def findMax():
    length = len(strN)
    queue = deque()
    queue.append((K, strN))
    beforeCnt = K + 1
    answer = -1

    while queue:
        cnt, curArr = queue.popleft()

        if cnt == 0:
            answer = max(answer, int(''.join(curArr)))
            continue

        if beforeCnt != cnt:
            visit = set()

        for i in range(length):
            for j in range(i+1, length):
                nextArr = curArr[:]
                nextArr[i], nextArr[j] = nextArr[j], nextArr[i]
                if nextArr[0] != '0' and ''.join(nextArr) not in visit:
                    queue.append((cnt - 1, nextArr))
                    visit.add(''.join(nextArr))

        beforeCnt = cnt
    
    return answer


N, K = map(int, sys.stdin.readline().split())
answer = -1
strN = []
while N > 0:
    strN.append(str(N%10))
    N //= 10
strN = strN[::-1]
print(findMax())