# !!! heappq 를 사용해야 속도 통과


def solution(scoville, K):
    answer = 0

    while min(scoville) < K:
        if len(scoville) == 1:
            answer = -1
            break

        scoville.sort()
        min_1 = scoville.pop(0)
        min_2 = scoville.pop(0)
        #min_1 = scoville.pop(scoville.index(min(scoville)))
        #min_2 = scoville.pop(scoville.index(min(scoville)))

        scoville.append(min_1 + min_2 * 2)

        answer += 1

    return answer




a = [1, 2, 3, 9, 10, 12]
b = 7
print(solution(a, b))