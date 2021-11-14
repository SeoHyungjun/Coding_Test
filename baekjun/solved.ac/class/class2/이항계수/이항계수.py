def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)

n, k = map(int, input().split())

if k < 0:
    print('0')
elif k > n:
    print('0')
else:
    print(factorial(n)//(factorial(k)*factorial(n-k)))