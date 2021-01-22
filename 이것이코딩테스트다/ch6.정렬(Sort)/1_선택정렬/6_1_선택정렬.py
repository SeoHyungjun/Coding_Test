array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)


# 선택 정렬의 시간복잡도
# 선택 정렬의 경우 n-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보낸다.
# 또한, 매번 가장 작은 수를 찾기 위해서 비교 연산이 필요한다.
# 앞의 코드의 경우 N + (N - 1) + (N - 2) + ... + 2 로 볼 수 있다.
# 즉, N * (N + 1) / 2이므로 (N^2) + N / 2 이다.
# 빅오표기법으로 나타내면, O(N^2)