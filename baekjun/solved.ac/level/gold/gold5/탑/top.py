import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
stack=[]
ans=[]
for i in range(n):
    while 1:
        print(stack, ans)
        if not stack:
            print(1)
            stack.append((i,arr[i]))
            ans.append(0)
            break
        if stack[-1][1]>=arr[i]:
            print(2)
            ans.append(stack[-1][0]+1)
            stack.append((i,arr[i]))
            break
        else:
            print(3)
            stack.pop()
print(*ans)
