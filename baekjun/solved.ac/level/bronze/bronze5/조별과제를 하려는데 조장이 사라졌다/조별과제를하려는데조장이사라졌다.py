import sys

L = int(sys.stdin.readline())

print(L//5 + 1 if L%5 else L//5)