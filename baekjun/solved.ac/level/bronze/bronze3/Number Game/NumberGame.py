import sys

def func(x, b):
    if x != 0 and x % b == 0:
        return 1 + func(x//b, b)
    return 0
    
sum_of_func = [0] * 1001
for i in range(2, 1001):
    sum_of_func[i] = sum(func(i, b) for b in range(2, i+1))

for _ in range(int(sys.stdin.readline())):
    print(sum_of_func[int(sys.stdin.readline())])