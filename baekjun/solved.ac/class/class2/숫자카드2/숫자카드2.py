n = int(input())
sang = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

dic = {}
for sa in sang:
    if sa in dic:
        dic[sa] += 1
    else:
        dic[sa] = 1

for ch in check:
    if ch in dic:
        print(dic[ch], end = ' ')
    else:
        print('0', end = ' ')