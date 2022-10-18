import sys

N = int(sys.stdin.readline())
mod = N % 8
if mod == 1 : print(1)
elif mod == 2 or mod == 0 : print(2)
elif mod == 3 or mod == 7 : print(3)
elif mod == 4 or mod == 6 : print(4)
else : print(5)