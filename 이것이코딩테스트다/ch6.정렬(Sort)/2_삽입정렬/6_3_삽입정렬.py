arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] > arr[j-1]:
            break
        else:
            arr[j], arr[j-1] = arr[j-1], arr[j]

print(arr)

# 삽입정렬의 시간 복잡도
# 1, 2, 3, ...., n 번 실행되므로
# n + n-1 + n-2 + ... + 1 = n * (n-1) / 2 = n^2 - n
# 즉, O(n^2)