import sys

dic = {3:'A', 2:'B', 1:'C', 0:'D', 4:'E'}
for _ in range(3):
    print(dic[sum(map(int, sys.stdin.readline().split()))])