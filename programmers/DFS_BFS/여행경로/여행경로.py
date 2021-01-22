# 210122 14:06 -> 14:28 + 16:05 -> 16:33

# operator(1,2)의 경우
# 인자 1로 정렬 하지만 같을 경우 2로 정렬

# a = []
# b = a 하면 a = b가 되어서 b를 수정하여도 a가 같이 수정되는것....
# b = a[:] 로 하면 복사를 하여서 b를 수정하여도 a가 수정 x

from operator import itemgetter
from collections import deque

def solution(tickets):
    answer = []
    total_len = len(tickets)

    tickets.sort( key = itemgetter(0,1))
    queue = deque()
    queue.append(('ICN', answer, tickets))

    while queue:
        cur, load, ticket = queue.popleft()

        if len(ticket) == 0 and len(load) == total_len:
            load.append(cur)
            return load

        for ti in ticket:
            if ti[0] == cur:
                next_ticket = ticket[:]
                next_ticket.remove(ti)
                queue.append((ti[1], load + [cur], next_ticket))





t = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
t = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(solution(t))