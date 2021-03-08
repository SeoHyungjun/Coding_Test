
from itertools import combinations as combi
from itertools import permutations as permu

import copy

def solution(n, weak, dist):
    answer = 0

    sorted_dist = copy.deepcopy(dist)
    # dist는 친구들이 이동할 수 있는 거리, 즉 큰수부터 확인해야지 정답을 빠르게 찾을 수 있음
    sorted_dist.sort(reverse = True)

    # 투입되는 친구의 수, 1부터 시작하며, 작은수부터 커지므로 만약 weak를 다 확인할 경우 그게 최소값
    for i in range(1, len(dist)+1):
        
        # weak 중 i개 선택 (친구의 수 만큼 선택)
        for start in permu(weak, i):
            # 각 경우 (weak에서 i개를 선택했을 때마다 weak를 따로 관리 -> new_weak)
            new_weak = copy.deepcopy(weak)
            #print(start)
            # 선택된 점의 index와 값 선택
            for index, st in enumerate(start):
                #print(index, st)
                # 선택된 점에서 sorted_dist(친구)중 멀리 이동할 수 있는 친구부터 이동하면서 new_weak를 지나칠 경우 체크
                #print(st, '~', st, '+', sorted_dist[index])

                for j in range(len(new_weak)-1, -1, -1):
                    # st + sorted_dist[index]+1 > 12
                    if st + sorted_dist[index]+1 >= n:
                        if 0 <= new_weak[j] <= (st+sorted_dist[index])%n or st <= new_weak[j] < n:
                            del new_weak[j]
                    # < 12
                    else:
                        if st <= new_weak[j] <= st+sorted_dist[index]:
                            del new_weak[j]
                #print(new_weak)

                '''
                    #print(st%n, new_weak[j], (st+sorted_dist[index]))
                    if st <= new_weak[j] <= (st+sorted_dist[index]) or ( st+sorted_dist[index] > 12 and new_weak[j] <= (st+sorted_dist[index])%n):
                        del new_weak[j]
                    #print(new_weak, '\n')
                
                for check in range(st, st+sorted_dist[index]+1):
                    # 만약 이동 중 new_weak 지점을 지날경우 삭제
                    if check%n in new_weak:
                        #new_weak.remove(check%n)
                        del new_weak[new_weak.index(check%n)]
                '''

            # weak에서 i개의 점을 선택하여 이동 거리만큼 지나면서 모든 weak를 지나쳤을 경우 투입된 친구의 수(i) 리턴
            if not new_weak:
                #print('end')
                return i
            
    # 모든 경우를 다 체크하였지만, 모든 weak를 다 돌지 못 할 경우 -1 리턴
    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print()
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print()
print(solution(200, [0,100], [1,1]))