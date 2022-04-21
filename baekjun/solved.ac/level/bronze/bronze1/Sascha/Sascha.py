import sys

def diff_alpha(a, b):
    cnt = 0

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        cnt += 1

    return cnt

N = int(sys.stdin.readline())
for _ in range(N):
    sascha = sys.stdin.readline().rstrip()
    avail = []
    min_diff = float('inf')

    W = int(sys.stdin.readline())
    for _ in range(W):
        word = sys.stdin.readline().rstrip()
        cur_diff = diff_alpha(sascha, word)

        if cur_diff < min_diff:
            min_diff = cur_diff
            avail = [word]

    print(avail[0])