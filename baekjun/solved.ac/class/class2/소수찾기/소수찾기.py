n = int(input())

li = list(map(int, input().split()))

max_num = max(li)
prime = [True] * (max_num+1)
for i in range(2, int(max_num**0.5)+1):
    if prime[i]:
        for j in range(2*i, max_num+1, i):
            prime[j] = False

cnt = 0
for i in li:
    if i != 1 and prime[i]:
        cnt += 1

print(cnt)