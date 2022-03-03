import sys
import math

N = int(sys.stdin.readline())
file_size =list(map(int, sys.stdin.readline().split()))
cluster_size = int(sys.stdin.readline())

cluster_num = 0
for file in file_size:
    if file == 0:
        continue

    cluster_num += math.ceil(file / cluster_size)

print(cluster_size * cluster_num)