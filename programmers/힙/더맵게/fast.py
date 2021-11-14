# !!! heappq 를 사용해야 속도 통과

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break

        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        
    return answer

a = [1, 2, 3, 9, 10, 12]
b = 7
print(solution(a, b))