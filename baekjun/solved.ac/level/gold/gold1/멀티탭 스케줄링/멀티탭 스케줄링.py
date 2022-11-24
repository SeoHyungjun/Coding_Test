import sys
from collections import defaultdict, deque

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(deque)
for idx, n in enumerate(arr): dic[n].append(idx)

multi_tap = set()
answer = 0
for cur in arr:
    dic[cur].popleft()
    if cur in multi_tap: continue
    if len(multi_tap) >= N:
        # 연결된 전기용품 중 앞으로 사용안되는게 있는지 체크
        flag = -1
        for connected in multi_tap:
            if dic[connected]: continue
            flag = connected
            break
        
        # 모두 앞으로 다시 연결해야 하므로 가장 나중에 연결해야하는 것 찾기
        if flag == -1:
            max_uesd_time = -1
            for connected in multi_tap:
                if dic[connected][0] <= max_uesd_time: continue
                max_uesd_time = dic[connected][0]
                flag = connected

        multi_tap.remove(flag)
        answer += 1

    multi_tap.add(cur)

print(answer)