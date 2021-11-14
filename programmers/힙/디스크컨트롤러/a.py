import heapq

def solution(jobs):
    jobs.sort()
    cur_time = jobs[0][0]
    total_len = len(jobs)
    count = 0
    heap = []
    answer = []

    while count < total_len:
        while len(jobs) > 0 and cur_time >= jobs[0][0]:
            heapq.heappush(heap, (jobs[0][1], jobs[0][0]))
            jobs.pop(0)

        if len(heap) > 0:
            time, start = heapq.heappop(heap)
            cur_time += time
            answer.append(cur_time - start)
            count += 1
        else:
            cur_time += 1

    return sum(answer)//total_len


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
