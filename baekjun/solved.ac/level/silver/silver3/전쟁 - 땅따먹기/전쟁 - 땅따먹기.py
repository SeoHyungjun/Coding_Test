import sys
from collections import Counter

N = int(sys.stdin.readline())
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    T, arr = arr[0], arr[1:]

    cnt = Counter(arr)
    answer = "SYJKGW"
    for country in cnt:
        if cnt[country] > T/2:
            answer = country
            break

    print(answer)