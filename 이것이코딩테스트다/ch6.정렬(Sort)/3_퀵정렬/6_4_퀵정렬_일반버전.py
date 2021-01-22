arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)


# 시간 복잡도 O(NlogN) -> 일반적으로,,,,, 최악의 경우 O(N^2)
# logN 은 log(2)N을 의미 (밑이 2인)
# 
# 퀵정렬의 경우 재귀호출을 사용
# 재귀호출을 하기 전 N개의 원소를 비교
# 그 뒤에 재귀호출이 된다면 n/2만큼 2번의 원소를 비교

# -> T(N) = 2*T(N/2) + N = 