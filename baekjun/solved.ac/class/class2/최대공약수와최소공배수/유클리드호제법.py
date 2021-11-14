# 유클리드 호제법으로 최대공약수 구하기
# 큰 수가 항상 a
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 최대공약수와 두 수를 사용하여 최소공배수 lcm 구하기
def lcm(a, b):
    return a*b//gcd(a,b)

a, b = map(int, input().split())

print(gcd(max(a,b), min(a,b)))
print(lcm(max(a,b), min(a,b)))
