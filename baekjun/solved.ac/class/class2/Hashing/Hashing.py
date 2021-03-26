import sys

L = int(sys.stdin.readline())
string_list = list(sys.stdin.readline())

a_num = -ord('a')+1

#new_list = [((ord(string_list[i])+a_num)*(31**i))%1234567891 for i in range(len(string_list))]
answer = 0
start = 1

for i in range(L):
    answer += ((ord(string_list[i]) + a_num) * start)
    start *= 31

print(answer % 1234567891)
