import sys

checknum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
select = [0 for i in range(3)]
isStop = False

def dfs(cnt) :
    global isStop
    global select
    
    if isStop:
        return 
    
    if cnt == 3:
        checklist = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(3):
            for j in range(3):
                checklist[i][j] = count[i][j] * select[i]
        
        isAns = True
        for i in range(3):
            if checklist[0][i] + checklist[1][i] != checklist[2][i]:
                isAns = False
                break
        
        if isAns:
            isStop = True
            for i in range(3):
                print(select[i], end=" ")
        return 
    
    for i in range(10):
        select[cnt] = checknum[i]
        dfs(cnt + 1)
        


str = input()
list = str.replace('+', ' ').replace('=', ' ').split(' ')
list[0] = list[0] + ' '
list[1] = list[1] + ' '
list[2] = list[2] + ' '

count = []
for s in list:
    tmp = [0, 0, 0]
    
    for i in range(len(s)):
        if s[i].isdigit():
            continue
        
        num = 1
        if s[i] == 'C':
            if s[i+1].isdigit():
                num = int(s[i+1]) 
            tmp[0] += num
            
        elif s[i] == 'H':
            if s[i+1].isdigit():
                num = int(s[i+1]) 
            tmp[1] += num
            
        elif s[i] == 'O':
            if s[i+1].isdigit():
                num = int(s[i+1]) 
            tmp[2] += num
    
    count.append(tmp)
    
dfs(0)