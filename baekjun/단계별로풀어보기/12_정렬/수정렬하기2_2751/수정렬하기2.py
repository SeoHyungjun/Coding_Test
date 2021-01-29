from sys import stdin as st

n = int(st.readline())
arr = []

for i in range(n):
    arr.append(int(st.readline()))

arr.sort()

for i in range(n):
    print(arr[i])