# 2021-02-24 21:20 ->

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    for city in cities:
        # cache hit
        if city.lower() in q:
            q.remove(city.lower())
            q.append(city.lower())
            answer += 1

        # cache miss
        else:
            if cacheSize > 0:
                if len(q) > cacheSize - 1:
                    q.popleft()
                q.append(city.lower())
            answer += 5

    return answer


cacheSize = 5
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
#cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))