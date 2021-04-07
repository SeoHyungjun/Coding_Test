import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    dic = {}

    for _ in range(N):
        name, cloth = sys.stdin.readline().rstrip().split()
        
        if cloth not in dic:
            dic[cloth] = [name]
        else:
            dic[cloth].append(name)

    answer = 1
    for clo in dic:
        answer *= len(dic[clo]) + 1

    print(answer - 1)
