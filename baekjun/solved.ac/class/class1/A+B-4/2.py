# import sys

# for i in sys.stdin:
#     print(sum(list(map(int, i.split()))))

import sys

for line in sys.stdin:

    a,b = map(int, line.split())

    print(a+b)