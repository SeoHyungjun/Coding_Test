import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    word = sys.stdin.readline().rstrip('\n')
    if word not in arr:
        arr.append(word)

arr.sort(key = lambda x : (len(x), x))

for word in arr:
    print(word)