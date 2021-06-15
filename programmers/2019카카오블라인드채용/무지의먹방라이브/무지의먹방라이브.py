def solution(food_times, k):
    answer = 0
    bak = []
    for i in range(len(food_times)):
        bak.append([food_times[i], i+1])
    food_times = bak

    while True:
        if not food_times:
            return -1

        if len(food_times) > k:
            return food_times[k%len(food_times)][1]

        else:
            min_val = 1
            if min(food_times)[0] > k%len(food_times):
                min_val = k%len(food_times)

            del_index = []
            len_food = len(food_times)
            for i in range(len_food):
                food_times[i][0] -= 1 * min_val
                if food_times[i][0] <= 0:
                    del_index.append(i)

            del_index.sort(reverse=True)
            for i in del_index:
                del food_times[i]

            answer += len_food*min_val
            k -= len_food

print(solution([3, 1, 2], 5))
print(solution([1,1,1,1], 4))