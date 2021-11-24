import sys

size_of_number = {'0':4, '1':2, '2':3, '3':3, '4':3, '5':3, '6':3, '7':3, '8':3, '9':3}

while True:
    input_number = int(sys.stdin.readline())

    if input_number == 0:
        break

    total_size = 1
    for s in str(input_number):
        total_size += size_of_number[s] + 1

    print(total_size)