import heapq

def solution(operations):
    answer = []
    heap = []

    for op in operations:
        split_op = op.split()

        if split_op[0] == 'I':
            heapq.heappush(heap, int(split_op[1]))

        else:
            if len(heap) == 0:
                continue

            if split_op[1] == '-1':
                heapq.heappop(heap)

            elif split_op[1] == '1':
                new_heap = []
                while heap:
                    if len(heap) == 1:
                        heap = new_heap
                        break
                    else:
                        heapq.heappush(new_heap, heapq.heappop(heap))

    if len(heap) == 0:
        return [0, 0]
    return [max(heap), min(heap)]


operations = ['I 16','D 1']
#operations = ['I 7','I 5','I -5','D -1']
print(solution(operations))