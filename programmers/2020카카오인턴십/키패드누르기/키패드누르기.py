# 2021-03-05 18:08 ->

def solution(numbers, hand):
    answer = ''
    pad = {1:(0,0), 2:(1,0), 3:(2,0), 4:(0,1), 5:(1,1), 6:(2,1), 7:(0,2), 8:(1,2), 9:(2,2), 0:(1,3)}
    left = (0,3)
    right = (2,3)
    leftside = [1, 4, 7]
    rightside = [3, 6, 9]
    other = [2, 5, 8, 0]

    for number in numbers:
        print(number, number in leftside)
        if number in leftside or (number in other and abs(left[0]-pad[number][0]) + abs(left[1]-pad[number][1]) < abs(right[0]-pad[number][0]) + abs(right[1]-pad[number][1])):
            answer += 'L'
            left = pad[number]
        elif number in rightside or (number in other and abs(left[0]-pad[number][0]) + abs(left[1]-pad[number][1]) > abs(right[0]-pad[number][0]) + abs(right[1]-pad[number][1])):
            answer += 'R'
            right = pad[number]
        else:
            answer += hand[0].upper()
            if hand == 'left':
                left = pad[number]
            else:
                right = pad[number]

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))