T = int(input())

li = []

for _ in range(T):
    a = int(input())
    b = int(input())

    li.append((a, b))

apart = [[0] * max(li, key=lambda x : x[1])[1] for _ in range(1+max(li, key=lambda x : x[0])[0])]

for i in range(max(li, key=lambda x : x[1])[1]):
    apart[0][i] = i+1

for i in range(1, 1+max(li, key=lambda x : x[0])[0]):
    for j in range(max(li, key=lambda x : x[1])[1]):
        apart[i][j] = sum(apart[i-1][:j+1])

for a,b in li:
    print(apart[a][b-1])