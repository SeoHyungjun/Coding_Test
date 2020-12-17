N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse = True)

# 가장 큰 수가 더해지는 경우와 두번째로 큰 수가 더해지는 경우로 나누어 생각해보면
# M만큼의 길이 중 K번까지는 가장 큰 수, 그 다음 두번째로 큰 수
# 즉, K + 1번마다 두번째로 큰 수 등장
# K가 3일 경우
# 1 1 1 2 / 1 1 1 2 / 1 1 1 2 / ~~~~~
# 가장 큰 수는 int( M / ( K + 1 ) ) * K 번 더하고, 마지막 범위에서 나머지인 M % ( K + 1 ) 번 더하게 된다.
# 두번째로 큰 수는 M - (가장 큰 수를 더한 횟수) 번 더하게 된다.

first = int(M/(K+1))*K + M%(K+1)
second = M - first

sum = first * num[0] + second * num[1]

print(sum)