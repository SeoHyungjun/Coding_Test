import sys
import math

N = sys.stdin.readline().rstrip()
digit = set(list(N))

lcm = 1
for i in digit:
    if int(i) == 0:
        continue
    lcm = lcm * int(i) // math.gcd(lcm, int(i))

multi_ten = 1
flag = True
while flag:
    for i in range(multi_ten):
        if (int(N) * multi_ten + i) % lcm == 0:
            flag = False
            answer = int(N)*multi_ten + i
            break

    multi_ten *= 10

print(answer)