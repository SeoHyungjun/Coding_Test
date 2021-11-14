n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2

    get_tree = sum([tree - mid if tree > mid else 0 for tree in trees])

    if get_tree >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)