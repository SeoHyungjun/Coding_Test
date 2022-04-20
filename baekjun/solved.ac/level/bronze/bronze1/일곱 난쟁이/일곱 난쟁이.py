import sys

length = [int(sys.stdin.readline()) for _ in range(9)]
length.sort()
sum_length = sum(length)

end_flag = False
for i in range(9):
    for j in range(i+1, 9):
        if sum(length) - length[i] - length[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(length[k])

            end_flag = True
            break
            
    if end_flag:
        break