import sys

arr = []
for i in range(1, 6):  
    name = sys.stdin.readline().rstrip()
    if "FBI" in name:  
        arr.append(i)  
print(*arr) if arr else print("HE GOT AWAY!")