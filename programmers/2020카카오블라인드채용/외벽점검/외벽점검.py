# 2021-03-07 18:27 -> 유튭 보고따라함....

import copy
from itertools import combinations as combi

def solution(n, weak, dist):
    dst = copy.deepcopy(dist)
    dst.sort(reverse = True)

    # 투입되는 친구의 수
    for i in range(1, len(dst)+1):
        # weak = [1, 5, 6, 10]
        for item in combi(range(len(weak)), i):
            # i = 2  -> (0,1), (0,2), (0,3), ....
            d = []
            for j in range(i):
                d.append((weak[item[(j+1)%i]-1] - weak[item[j]] + n) % n)
            d.sort(reverse=True)

            rst = True
            for j in range(i):
                if dst[j] < d[j]:
                    rst = False

            # weak 중 i개의 점을 선택하여 큰 dst부터 거리 체크하여
            # 모든 weak 다 확인할 경우
            if rst:
                return i

    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))