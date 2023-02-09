import sys

s1, s2 = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(s1)]
for i in range(s1):
    if arr[i][0] == arr[i][1]: continue
    print("Wrong Answer")
    exit()

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(s2)]
for i in range(s2):
    if arr[i][0] == arr[i][1]: continue
    print("Why Wrong!!!")
    exit()
        
print("Accepted")