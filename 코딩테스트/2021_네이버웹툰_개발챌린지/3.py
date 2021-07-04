def solution(arr, k):
    answer = 0

    len_arr = len(arr)
    start = len_arr

    while start > 0:
        print(arr)
        i = arr.index(start)

        if i == start - 1:
            start -= 1
            continue

        min_index = i
        for j in range(1, k+1):
            if i + j < len_arr:
                if i + j == start - 1:
                    min_index = i + j
                    break

                if arr[min_index] > arr[i+j]:
                    min_index = i + j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print('answr += 1')
            answer += 1

    return answer


print(solution([4,5,2,3,1], 2))
print(solution([5,4,3,2,1], 4))
print(solution([5,4,3,2,1], 4))