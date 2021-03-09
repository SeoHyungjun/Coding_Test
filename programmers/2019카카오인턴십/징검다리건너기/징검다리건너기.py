# 2021-03-09 19:30 -> 19:53

def check(mid, stones, k):
    long_cnt = 0

    for i in range(len(stones)):
        if stones[i] - mid <= 0:
            long_cnt += 1
        else:
            long_cnt = 0

        if long_cnt >= k:
            return '더작게'
    return '더크게'


def solution(stones, k):
    answer = 0

    small, big = 1, 200000000

    while small < big-1:
        mid = (small + big) // 2
        if check(mid, stones, k) == '더크게':
            small = mid
        else:
            big = mid

    return big

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))