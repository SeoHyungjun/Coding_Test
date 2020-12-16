H, W = map(int, input().split())

wall = list(map(int, input().split()))

#print(wall)

a = 0
result = 0

for i in range(0, W):
    if wall[i] != 0:
        a = i
        break

#print('left')
for i in range( a, wall.index(max(wall)) + 1 ):
    if i != a and wall[i] >= wall[a] :
        for j in range(a + 1, i):
            result = result + ( wall[a] - wall[j] )
        a = i


for i in range(W-1, 0, -1):
    if wall[i] != 0:
        a = i
        break

#print('right')
for i in range( a, wall.index(max(wall)) - 1, -1):
    if i != a and wall[i] >= wall[a] :
        for j in range(a - 1, i, -1):
            result = result + (wall[a] - wall[j])
        a = i

print(result)