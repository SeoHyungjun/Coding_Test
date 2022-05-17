import sys

user_input = sys.stdin.readline().rstrip()
num_arr = [0]*10
for a in user_input:
    num_arr[int(a)] += 1

while abs(num_arr[6] - num_arr[9]) > 1:
    if num_arr[6] > num_arr[9]:
        num_arr[6] -= 1
        num_arr[9] += 1
    else:
        num_arr[6] += 1
        num_arr[9] -= 1

print(max(num_arr))