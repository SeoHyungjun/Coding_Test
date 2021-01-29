import sys 
from collections import Counter

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 산술 평균
print(round(sum(arr)/n))

# 중앙 값
arr.sort()
print(arr[n//2])

# 최빈 값
k = Counter(arr).most_common()
print(k)

if len(k) > 1 and k[0][1] == k[1][1]:
        print(k[1][0])
else:
    print(k[0][0])

# 범위
print(max(arr) - min(arr))