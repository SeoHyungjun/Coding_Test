import sys

def findMintime():
    N = int(sys.stdin.readline())
    crane = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    M = int(sys.stdin.readline())
    box = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    if crane[0] < box[0]:
        return -1

    cnt = [0] * N

    for i in box:
        index = 0
        for j in range(N):
            if i <= crane[j] and cnt[index] > cnt[j]:
                index = j
            elif i > crane[j]:
                break
        cnt[index] += 1

    return max(cnt)

print(findMintime())