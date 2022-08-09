import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
user_set = sorted(list(sys.stdin.readline().split()))
vowels = set(['a', 'e', 'i', 'o', 'u'])

for comb in combinations(user_set, L):
    len_vowels = len(set(comb) & vowels)
    if len_vowels < 1 or len(set(comb) - vowels) < 2:
        continue
    if sorted(comb) != list(comb):
        continue
    print(''.join(comb))