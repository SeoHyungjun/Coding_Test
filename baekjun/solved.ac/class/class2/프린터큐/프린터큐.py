num = int(input())

for _ in range(num):
    n, m = map(int, input().split())

    li = list(map(int, input().split()))

    cnt = 0

    while True:
        if li[0] == max(li):
            li.pop(0)
            cnt += 1
            if m == 0:
                print(cnt)
                break
        else:
            li.append(li.pop(0))
        m = (m + len(li) -1) % len(li)