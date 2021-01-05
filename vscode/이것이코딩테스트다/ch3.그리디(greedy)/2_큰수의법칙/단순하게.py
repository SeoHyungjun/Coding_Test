N, M, K = map(int, input().split())
num = list(map(int, input().split()))


print(N, M, K)
print(num)

num.sort(reverse = True)
print(num)

check_k = 0
sum = 0

while M > 0:
    if check_k >= K:
        sum += num[1]
        check_k = 0
    else:
        sum += num[0]
        check_k += 1
    M -= 1

print(sum)