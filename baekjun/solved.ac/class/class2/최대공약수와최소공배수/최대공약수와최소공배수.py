a, b = map(int, input().split())

for i in range(min(a,b), 0, -1):
    if a%i == 0 and b%i == 0:
        max_num = i
        break

print(i)
print(i  * (a//i) * (b//i))
