k, n = map(int, input().split())

li = []

for _ in range(k):
    li.append(int(input()))

start = 1
end = max(li)

while start <= end:
    mid = (start+end)//2

    cnt = sum([ i//mid for i in li ])

    if cnt >= n:
        start = mid+1
    else:
        end = mid-1

print(end)