import sys

user_input = list(map(int, sys.stdin.readline().split()))
A = [user_input[0], user_input[1]]
B = [user_input[2], user_input[3]]
C = [user_input[4], user_input[5]]

#if ( (A[0] - B[0])/(A[1] - B[1]) == (B[0] - C[0])/(B[1] - C[1]))
if ( (A[0] - B[0])*(B[1] - C[1]) == (B[0] - C[0])*(A[1] - B[1])):
    print(-1.0)
    exit()

len_AB = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5
len_BC = ((B[0] - C[0])**2 + (B[1] - C[1])**2)**0.5
len_CA = ((C[0] - A[0])**2 + (C[1] - A[1])**2)**0.5

length = [len_AB + len_BC, len_BC + len_CA, len_CA + len_AB]
answer = (max(length) - min(length))*2

print(answer)