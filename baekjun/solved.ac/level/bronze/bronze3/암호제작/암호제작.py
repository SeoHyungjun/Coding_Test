import sys

def find_prime():
    prime_list = [True] * K
    prime_list[0] = False
    prime_list[1] = False
    return_prime_list = []

    for i in range(2, int(K**0.5) + 1):
        if prime_list[i]:
            for j in range(2*i, K, i):
                prime_list[j] = False

    for i in range(2, K):
        if prime_list[i]:
            return_prime_list.append(i)

    return return_prime_list

P, K = map(int, sys.stdin.readline().split())

prime_list = find_prime()
good_flag = True
for i in range(len(prime_list)):
    if P % prime_list[i] == 0:
        good_flag = False
        break

if good_flag:
    print('GOOD')
else:
    print('BAD', prime_list[i])