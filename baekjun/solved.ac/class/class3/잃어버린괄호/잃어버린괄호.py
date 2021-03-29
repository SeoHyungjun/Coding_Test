arr = input().split('-')
answer = 0

def sum_arr(ar):
    sum_ar = 0
    for i in ar.split('+'):
        if i != '+':
            sum_ar += int(i)

    return sum_ar

if arr[0] != '':
    answer = int(sum_arr(arr[0]))

for i in arr[1:]:
    answer -= sum_arr(i)

print(answer)