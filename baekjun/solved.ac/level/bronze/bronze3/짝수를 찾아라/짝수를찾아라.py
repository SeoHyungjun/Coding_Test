import sys

for _ in range(int(sys.stdin.readline())):
    min_even = float('inf')
    sum_even = 0
    for n in map(int, sys.stdin.readline().split()):
        if n % 2 == 0:
            sum_even += n
            min_even = min(min_even, n)
            
    print(sum_even, min_even)