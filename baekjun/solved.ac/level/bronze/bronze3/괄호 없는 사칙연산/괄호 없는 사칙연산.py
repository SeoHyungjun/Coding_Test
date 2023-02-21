import sys

def f(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return -1*(abs(a) // abs(b)) if a * b < 0 else a // b

arr = list(sys.stdin.readline().split())

arr[0] = int(arr[0])
arr[2] = int(arr[2])
arr[4] = int(arr[4])

a = f(f(arr[0], arr[2], arr[1]), arr[4], arr[3])
b = f(arr[0], f(arr[2], arr[4], arr[3]), arr[1])

print(min(a, b))
print(max(a, b))