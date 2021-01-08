N = int(input())

cnt = 0

for i in range(0, N+1):
    for j in range(60):
        for k in range(60):
            #if i//10== 3 or i%10 == 3 or j//10 == 3 or j%10 == 3 or k//10 == 3 or k%10 == 3:
            if '3' in str(i) + str(j) + str(k):
                print(i, j, k)
                cnt += 1
print(cnt)