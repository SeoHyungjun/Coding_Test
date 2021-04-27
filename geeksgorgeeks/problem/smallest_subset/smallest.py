import sys
from itertools import combinations

arr = list(map(int, sys.stdin.readline().split(',')))
maximum = 0
combi_list = []
min_len = len(arr)

for i in range(1, len(arr)+1):
    for j in list(combinations(arr, i)):
        ans = 0
        for k in j:
            ans |= k

        if ans > maximum:
            maximum = ans
            combi_list = [j]
            min_len = len(j)

        elif ans == maximum and min_len == len(j):
            combi_list.append(j)

print(maximum)
print(combi_list)



"""
Input : arr[] = {5, 1, 3, 4, 2}
Output : 2
7 is the maximum value possible of OR, 
5|2 = 7 and 5|3 = 7

Input : arr[] = {2, 6, 2, 8, 4, 5}
Output : 3
15 is the maximum value of OR and set
elements are 8, 6, 5 
"""