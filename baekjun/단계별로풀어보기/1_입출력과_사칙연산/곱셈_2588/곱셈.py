a = int(input())
b = int(input())

di3 = a * (b%10)
b //= 10
di4 = a * (b%10)
b //= 10
di5 = a * (b%10)

print(di3)
print(di4)
print(di5)
print(((di5 * 10) + di4) * 10 + di3)