import sys

N = int(sys.stdin.readline())
candies=[]
ans = 1

for i in range(N):
    temp =[]
    temp_str = input()
    for j in range(N):
        temp.append(temp_str[j])
    candies.append(temp)
    
def search():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candies[i][j]== candies[i][j+1]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
        
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candies[j][i] == candies[j+1][i]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1

for i in range(N):
    for j in range(N-1):
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
        search()
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]

for i in range(N):
    for j in range(N-1):
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]
        search()
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]

print(ans)